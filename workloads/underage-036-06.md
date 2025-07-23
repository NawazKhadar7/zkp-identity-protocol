# underage-036-06

Reject a birthdate later than the verifier cutoff.

Input scale: 36; deterministic random seed: 137.
Run `python scripts/demo.py --case workloads/underage-036-06.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
