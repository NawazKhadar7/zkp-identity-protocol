# Additional scenarios for zkp-identity-protocol

Ten runnable scenarios cover small inputs, odd sizes, and behavior boundaries in the existing reference implementation.

This directory contains 10 input JSON files, 10 metric-oracle JSON files, 10 scenario notes, this guide, and the runner (32 files).

Run from the project directory with Python 3.10 or later and the dependencies already listed in requirements.txt.

~~~powershell
python -B examples/additional/run_cases.py --list
python -B examples/additional/run_cases.py
python -B examples/additional/run_cases.py --case valid-single --json
~~~

The runner exits with zero only when all selected scenarios pass. --json includes metrics and output or a failure reason for each scenario.

Each .case.json is paired with a .expected.json containing equality checks or numeric bounds for the existing syslab.common.check helper.
Scenario notes explain the selected boundaries. Fixed seeds make inputs repeatable; expected files contain assertions rather than recorded timings.

| Scenario | Family | Size | Purpose |
| --- | --- | --- | --- |
| valid-single | valid | 1 | Accept one valid reference credential. |
| valid-seven | valid | 7 | Accept seven credentials with distinct nonces. |
| underage-single | underage | 1 | Reject one underage credential. |
| underage-seven | underage | 7 | Reject seven underage credentials. |
| bad-commitment-single | bad-commitment | 1 | Reject one inconsistent commitment. |
| bad-commitment-nine | bad-commitment | 9 | Reject nine inconsistent commitments. |
| wrong-issuer-three | wrong-issuer | 3 | Reject three credentials from another issuer. |
| expired-single | expired | 1 | Reject one expired credential. |
| replayed-single | replayed | 1 | Reject a previously consumed nonce. |
| replayed-nine | replayed | 9 | Reject nine previously consumed nonces. |

Scope: Plaintext credential policy; no cryptographic ZK proof is generated.

Supplemental inputs have their own runner, so the existing workload discovery and its 36-case suite retain their current behavior.
Bytecode generation is disabled. Reports go to standard output; storage and model artifacts use the reference code's temporary directories.

See [limitations](../../docs/LIMITATIONS.md) and [running instructions](../../docs/RUNNING.md).
