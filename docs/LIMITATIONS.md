# Limitations

Default Python execution is NOT a ZK proof and reveals private fields to its evaluator. SHA-256/HMAC mocks are distinct from the Poseidon/EdDSA circuit and are not interoperable. Circom, circomlib and snarkjs execution/trusted setup were unavailable here; circuit and proof paths are unvalidated sources. No DID registry, revocation tree, Rust implementation or audited cryptographic protocol. A nonce ledger needs transactional storage and challenge expiry in a real service.
