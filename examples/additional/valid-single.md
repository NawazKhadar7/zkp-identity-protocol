# valid-single

Accept one valid reference credential.

The adult credential has a valid issuer and expiry.

Family: valid. Size: 1. Deterministic seed: 911201.

Run from the project directory:

~~~powershell
python -B examples/additional/run_cases.py --case valid-single
~~~

Add --json to inspect returned metrics and output.

The adjacent expected file specifies the following metric conditions:

| Metric | Condition |
| --- | --- |
| requests | equals 1 |
| accepted_in_reference | equals 1 |
| rejected | equals 0 |
| is_cryptographic_proof | equals false |
| replays_rejected | equals true |

Scope: Plaintext credential policy; no cryptographic ZK proof is generated.

These inputs are synthetic. See [project limitations](../../docs/LIMITATIONS.md).
