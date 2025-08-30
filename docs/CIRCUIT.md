# Optional cryptographic workflow

1. Install Circom 2 and `npm install`; run `sh scripts/compile_circuit.sh`.
2. Use an independently reviewed Powers of Tau and circuit-specific Groth16 contribution ceremony. Verify the final zkey, then export `verification_key.json` (follow official snarkjs documentation).
3. Prepare a request `{ "dob": 10957, "expiry": 21000 }`, a protected 32-byte issuer private key hex file and a trusted policy containing issuerAx, issuerAy, cutoff, now, nonce, audience as field-element strings. Choose a new random nonce for each challenge.
4. Run `node scripts/prove.mjs issue request.json key.txt policy.json artifacts/witness.json`. It produces a private Poseidon/EdDSA witness; confirm the derived issuer key equals policy.
5. Run `node scripts/prove.mjs prove artifacts/witness.json artifacts/circuit/credential_js/credential.wasm artifacts/credential_final.zkey artifacts/result`.
6. Run `node scripts/verify_proof.mjs artifacts/verification_key.json artifacts/result.public.json artifacts/result.proof.json policy.json artifacts/nonces.json`.

All paths above are optional and have not been executed in the generation environment. The verifier script is a serial local demo, not concurrent replay storage. Do not commit key or witness files.
