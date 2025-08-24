# underage-018-03

Reject a birthdate later than the verifier cutoff.

Input scale: 18; deterministic random seed: 134.
Run `python scripts/demo.py --case workloads/underage-018-03.case.json`.
The adjacent expected file specifies acceptance conditions independently from the implementation.
A successful run validates these conditions, not a production latency or capacity guarantee.

Inspect `metrics` and `output` in the returned JSON. Increase the input scale only after reading
`docs/LIMITATIONS.md`; do not extrapolate synthetic timing to hardware or external services.
