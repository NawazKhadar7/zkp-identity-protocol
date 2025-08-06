# valid-seven

Accept seven credentials with distinct nonces.

The ledger must not reject distinct valid requests.

Family: valid. Size: 7. Deterministic seed: 911202.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case valid-seven
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 7 |
| accepted_in_reference | equals 7 |
| rejected | equals 0 |
| is_cryptographic_proof | equals false |
| replays_rejected | equals true |

Scope: Plaintext credential policy; no cryptographic ZK proof is generated.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
