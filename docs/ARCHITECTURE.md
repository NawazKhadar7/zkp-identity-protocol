# Architecture

Default: mock issuer → plaintext policy checks → replay ledger. Optional: issuer EdDSA → private witness → Circom R1CS/WASM → Groth16 → verifier policy binding → nonce consumption.
