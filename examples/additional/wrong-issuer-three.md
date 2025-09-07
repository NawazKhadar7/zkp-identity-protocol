# wrong-issuer-three

Reject three credentials from another issuer.

Trusted issuer comparison rejects the whole batch.

Family: wrong-issuer. Size: 3. Deterministic seed: 911207.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case wrong-issuer-three
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 3 |
| accepted_in_reference | equals 0 |
| rejected | equals 3 |
| is_cryptographic_proof | equals false |
| replays_rejected | equals true |

Scope: Plaintext credential policy; no cryptographic ZK proof is generated.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
