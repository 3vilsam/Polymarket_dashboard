#!/usr/bin/env bash
# Restart the PAPER-only league engine forever (until STOP). Always warm the
# public candle cache before a start (--force), even when the lag is under
# 10 minutes. Back off 30–300s on failure; never give up. Alert in heartbeat.json.
# Does not loosen the 60s / no-stale-fills rule and never backfills fills.
set -u
cd -- "$(dirname -- "$(readlink -f -- "$0")")" || exit 1
if [[ -z "${SUPERVISE_STDBUF:-}" ]] && command -v stdbuf >/dev/null; then
  export SUPERVISE_STDBUF=1
  exec stdbuf -oL -eL "$0" "$@"
fi
exec 9>.supervisor.lock
flock -n 9 || exit 0
printf '%s\n' "$$" > supervisor.pid
child=''
quit() {
    trap - TERM INT
    if [[ -n "$child" ]]; then kill -TERM "$child" 2>/dev/null || true; wait "$child" 2>/dev/null || true; fi
    exit 0
}
trap quit TERM INT

alert() {
    local status=$1 backoff=$2 rc=${3:-} err=${4:-}
    python3 -u warm_cache.py --alert "$status" --backoff "$backoff" --engine-rc "$rc" --error "$err" --supervisor-pid "$$" >/dev/null
}

backoff=30
while [[ ! -e STOP ]]; do
    printf '%s supervisor warming public candle cache before restart (--force)\n' "$(date -Is)"
    alert SUPERVISOR_WARMING "$backoff" "" "warming cache before engine start"
    if ! python3 -u warm_cache.py --force --isolate; then
        printf '%s cache warm-up failed; backing off %ss without starting engine (no give-up)\n' "$(date -Is)" "$backoff"
        alert SUPERVISOR_WARM_FAILED "$backoff" "" "warm_cache.py failed; backing off, will retry"
        sleep "$backoff" &
        child=$!
        wait "$child" || true
        child=''
        (( backoff < 300 )) && backoff=$((backoff*2))
        (( backoff > 300 )) && backoff=300
        continue
    fi
    printf '%s supervisor starting PAPER-only engine\n' "$(date -Is)"
    alert SUPERVISOR_STARTING "$backoff" "" "starting league_v8.py (minute-aligned, boundary-skip)"
    began=$SECONDS
    python3 -u league_v8.py &
    child=$!
    printf '%s\n' "$child" > engine.pid
    wait "$child"
    rc=$?
    child=''
    rm -f engine.pid
    [[ -e STOP ]] && break
    printf '%s engine exited rc=%s; restarting after %ss (backoff, no give-up)\n' "$(date -Is)" "$rc" "$backoff"
    alert SUPERVISOR_RETRY "$backoff" "$rc" "engine exited rc=${rc}; will restart after backoff"
    if (( SECONDS - began > 600 )); then backoff=30; fi
    # Child wait is interruptible by TERM, unlike a foreground sleep.
    sleep "$backoff" &
    child=$!
    wait "$child" || true
    child=''
    (( backoff < 300 )) && backoff=$((backoff*2))
    (( backoff > 300 )) && backoff=300
done
