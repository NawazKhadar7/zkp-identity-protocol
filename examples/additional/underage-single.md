# underage-single

Reject one underage credential.

The age cutoff rejects the request.

Family: underage. Size: 1. Deterministic seed: 911203.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case underage-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 1 |
| accepted_in_reference | equals 0 |
| rejected | equals 1 |
| is_cryptographic_proof | equals false |
| replays_rejected | equals true |

Scope: Plaintext credential policy; no cryptographic ZK proof is generated.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
