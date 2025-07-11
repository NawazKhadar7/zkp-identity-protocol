# replayed-036-06

Reject reuse of an already consumed challenge.

Input scale: 36; deterministic random seed: 261.
Run `python scripts/demo.py --case workloads/replayed-036-06.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
