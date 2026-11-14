"""Append-only registry labels (labels-v1): NON_V1_RESEARCH promotion ineligibility, cluster tags, and
descriptive relabels. Display/evaluation-reporting overlay only; never edits rule files or hashes, never
changes sizing, signals or the DSR trial count (434)."""
import json
import league as L

STATUS_INELIGIBLE = 'INELIGIBLE_NON_V1_RESEARCH'

def load(root=L.ROOT):
    m = L.read_json(root/'registry/labels-v1.json')
    if L.sha(root/'registry/labels-v1.md') != m['note_sha256']: raise ValueError('labels-v1 note changed')
    return m

def tags(m, bid):
    out = []
    lab = m['labels'].get(bid)
    if lab: out.append(lab['label'])
    for c, ids in m['clusters'].items():
        if bid in ids: out.append(f'cluster:{c}')
    return out

def apply(st, m, now):
    """Annotate books; force promotion-ineligible status for NON_V1_RESEARCH books. Returns changed ids."""
    changed = []
    for bid, b in st['books'].items():
        lab = m['labels'].get(bid); cl = [c for c, ids in m['clusters'].items() if bid in ids]
        b['labels_v1'] = dict(label=lab['label'] if lab else None, description=lab['description'] if lab else None,
                              promotion_eligible=not (lab and lab.get('promotion_eligible') is False),
                              clusters=cl, note_sha256=m['note_sha256'])
        e = b.get('evaluation')
        if lab and lab.get('promotion_eligible') is False and e:
            if e.get('status') not in (STATUS_INELIGIBLE, 'CONTROL'):
                if e.get('status') in ('CANDIDATE_REVIEW_ONLY', 'FLAGGED_WAIT_FRESH_DAY', 'FLAGGED_WAIT_FRESH_DAY_FLAT', 'OOS_RUNNING', 'PAST_OOS_PASS_CURRENT_GATE_FAIL'):
                    if not b.get('ineligible_logged'):
                        L.event(b, 'promotion_ineligible', now, label=lab['label'], gate_status=e.get('status'), note_sha256=m['note_sha256'])
                        b['ineligible_logged'] = True
                e['gate_status_raw'] = e.get('status'); e['status'] = STATUS_INELIGIBLE
                changed.append(bid)
    return changed

def annotate_leaderboard(text, m):
    ids = set(m['labels']) | {i for v in m['clusters'].values() for i in v}
    for bid in sorted(ids, key=len, reverse=True):
        t = tags(m, bid)
        text = text.replace(f'| {bid} |', f"| {bid} [{', '.join(t)}] |").replace(f'| {bid} (RETIRED_DATA_QUALITY) |', f"| {bid} (RETIRED_DATA_QUALITY) [{', '.join(t)}] |")
    text += '\n## Labels and clusters (registry/labels-v1, append-only)\n\n'
    for bid, lab in m['labels'].items():
        text += f"- **{bid}**: {lab['label']} — {lab['description']}" + (' Promotion-ineligible.' if lab.get('promotion_eligible') is False else '') + '\n'
    text += '\nClusters (each cluster counts as ONE effective trial / one piece of independent evidence in any promotion review; the DSR multiplicity count stays 434, unchanged and conservative):\n'
    for c, v in m['clusters'].items(): text += f"- {c} ({len(v)} books): {', '.join(v)}\n"
    return text
