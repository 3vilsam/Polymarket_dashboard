#!/usr/bin/env bash
set -eu
cd -- "$(dirname -- "$(readlink -f -- "$0")")"
if [[ -e STOP ]]; then echo 'STOP file present; deliberately stopped. Remove only to resume paper league.'; exit 1; fi
if ! flock -n .supervisor.lock true; then
    echo "Paper league supervisor already locked/running; PID $(<supervisor.pid)"
    exit 0
fi
nohup ./supervise.sh </dev/null >>daemon.log 2>&1 &
echo "Started PAPER league supervisor launch PID $!; use ./status.sh for engine health"
