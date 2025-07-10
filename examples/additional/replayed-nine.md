# replayed-nine

Reject nine previously consumed nonces.

Replay rejection applies to the complete batch.

Family: replayed. Size: 9. Deterministic seed: 911210.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case replayed-nine
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 9 |
| accepted_in_reference | equals 0 |
| rejected | equals 9 |
| is_cryptographic_proof | equals false |
| replays_rejected | equals true |

Scope: Plaintext credential policy; no cryptographic ZK proof is generated.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
