# Zero-Knowledge Decentralized Identity Protocol

A credential policy reference plus an actual Circom age/expiry/signature circuit and optional Groth16 issuer/prover/verifier scripts.

This is newly generated educational reference code based on a concept in the supplied PDF.
It has **165 non-empty source, test, configuration, workload and documentation files**.
It is a prototype for study and extension, not evidence of previous deployment or measured large-scale performance.

## Quick start

Requires Python 3.10+; the default path uses the standard library.

```sh
python scripts/demo.py
python scripts/run_tests.py
python scripts/benchmark.py
python scripts/serve.py --port 8080
```

Open http://127.0.0.1:8080 for the workload dashboard. `scripts/demo.py --case workloads/<id>.case.json`
executes one workload and checks its independent acceptance conditions. `benchmark.py` prints actual local timings.

## Implemented scope

Default plaintext policy evaluator with HMAC mock credentials and replay ledger. Optional Circom circuit binds private DOB/expiry/salt to an issuer EdDSA-Poseidon signature, date cutoff and fresh audience/nonce. Node scripts issue witnesses, generate Groth16 proofs and verify trusted public signals.

## Limits and optional runtimes

Default Python execution is NOT a ZK proof and reveals private fields to its evaluator. SHA-256/HMAC mocks are distinct from the Poseidon/EdDSA circuit and are not interoperable. Circom, circomlib and snarkjs execution/trusted setup were unavailable here; circuit and proof paths are unvalidated sources. No DID registry, revocation tree, Rust implementation or audited cryptographic protocol. A nonce ledger needs transactional storage and challenge expiry in a real service.

All bundled data are synthetic. No credentials, pretrained model weights, historical commits, or fabricated benchmark results are included.
See `docs/PROVENANCE.md`, `docs/TESTING.md`, and the bundle's validation report for evidence and omissions.
