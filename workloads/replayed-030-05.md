# replayed-030-05

Reject reuse of an already consumed challenge.

Input scale: 30; deterministic random seed: 260.
Run `python scripts/demo.py --case workloads/replayed-030-05.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
