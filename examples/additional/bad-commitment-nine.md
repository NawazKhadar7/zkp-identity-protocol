# bad-commitment-nine

Reject nine inconsistent commitments.

Commitment consistency is enforced on every request.

Family: bad-commitment. Size: 9. Deterministic seed: 911206.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case bad-commitment-nine
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
