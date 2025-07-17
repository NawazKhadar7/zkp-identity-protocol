# underage-seven

Reject seven underage credentials.

Every request contributes to the rejected count.

Family: underage. Size: 7. Deterministic seed: 911204.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case underage-seven
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 7 |
| accepted_in_reference | equals 0 |
| rejected | equals 7 |
| is_cryptographic_proof | equals false |
| replays_rejected | equals true |

Scope: Plaintext credential policy; no cryptographic ZK proof is generated.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
