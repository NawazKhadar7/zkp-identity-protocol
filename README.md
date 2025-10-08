# Zero-Knowledge Decentralized Identity Protocol

A credential policy reference plus an actual Circom age/expiry/signature circuit and optional Groth16 issuer/prover/verifier scripts.

## 1. Overview

Credential verification must bind issuer authorization, eligibility rules and fresh verifier challenges. This project separates a runnable plaintext policy reference from optional Circom/Groth16 sources so application policy can be examined without misrepresenting it as a zero-knowledge proof.

**Project type:** educational reference implementation. **Repository contents:** 165 non-empty source, test, configuration, workload and documentation files, including 36 synthetic workload scenarios.

## 2. Core Features — Why They Matter

- **Eligibility policy reference:** Evaluates date-of-birth and expiry rules with mock HMAC credentials.
- **Replay handling:** Uses a nonce ledger to reject repeated challenges in the reference workflow.
- **Credential circuit source:** Includes a Circom circuit binding private credential fields to an EdDSA-Poseidon issuer signature and public challenge context.
- **Optional proof scripts:** Includes Node scripts for witness/proof generation and verification with policy-bound public signals.

## 3. Tech Stack & Architecture

| Layer | Technology | Implementation status |
| --- | --- | --- |
| Default execution | Python 3.10+, SHA-256/HMAC mock credentials | Runnable plaintext reference; not a ZK proof |
| Optional proof path | Circom 2, circomlib, snarkjs/Groth16, Node.js | Separate circuit and scripts; not executed in bundle validation |
| Proof artifacts | Compiled circuit, proving/verifying keys and trusted setup | Must be prepared and validated for the optional path |

### How the components fit together

The default workflow sends mock credentials through plaintext policy checks and a replay ledger. The optional workflow signs credential fields, builds a private witness, generates a Groth16 proof and checks public signals before consuming a verifier nonce. These workflows use different cryptographic primitives and are not interoperable.

| Component | Responsibility |
| --- | --- |
| [src/syslab/credentials.py](src/syslab/credentials.py) | Mock credentials and plaintext policy evaluation. |
| [src/syslab/nonce.py](src/syslab/nonce.py) | Challenge/replay ledger. |
| [circuits/credential.circom](circuits/credential.circom) | Optional signed age/expiry credential circuit source. |
| [scripts/verify_proof.mjs](scripts/verify_proof.mjs) | Optional proof verification and public-signal binding. |

See [Architecture](docs/ARCHITECTURE.md) and [Algorithms](docs/ALGORITHMS.md) for implementation notes.

### Scope and limitations

Default Python execution is NOT a ZK proof and reveals private fields to its evaluator. SHA-256/HMAC mocks are distinct from the Poseidon/EdDSA circuit and are not interoperable. Circom, circomlib and snarkjs execution/trusted setup were unavailable here; circuit and proof paths are unvalidated sources. No DID registry, revocation tree, Rust implementation or audited cryptographic protocol. A nonce ledger needs transactional storage and challenge expiry in a real service.

## 4. Getting Started / Installation

**Prerequisites:** Python 3.10+. The default reference uses Python's standard library. No API keys or external services are needed for the default sample.

Download/extract this project or clone its repository, then open a terminal in the `zkp-identity-protocol` folder. Create an isolated environment:

```sh
python -m venv .venv
```

Activate it on Linux/macOS:

```sh
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the declared Python dependencies and run the demo:

```sh
python -m pip install -r requirements.txt
python scripts/demo.py
```

Check behavior and collect timings on your own machine:

```sh
python scripts/run_tests.py
python scripts/benchmark.py
```

The original bundle validation recorded **20 passing tests** for this project and **36 accepted workload scenarios**. These are local reference checks, not production or hardware benchmarks. See [Testing](docs/TESTING.md) and [Benchmark notes](docs/BENCHMARKS.md).

The Circom/Node proof path has separate dependencies and requires validated circuit/setup artifacts. Review [the running guide](docs/RUNNING.md), [package.json](package.json) and the proof scripts before using that path. The Python demo remains a plaintext policy reference.

## 5. Usage Examples

### Run a reproducible workload

The bundled [sample request](examples/request.json) contains:

```json
{
  "family": "valid",
  "id": "valid-006-01",
  "seed": 101,
  "size": 6
}
```

Run the corresponding workload and check its independent acceptance conditions:

```sh
python scripts/demo.py --case workloads/valid-006-01.case.json
```

Expected `metrics` excerpt from the verified local run; the complete JSON also includes `output`:

```json
{
  "metrics": {
    "accepted_in_reference": 6,
    "is_cryptographic_proof": false,
    "rejected": 0,
    "replays_rejected": true,
    "requests": 6
  }
}
```

Six valid requests pass the plaintext reference policy and replay checks. The response explicitly states is_cryptographic_proof=false; no zero-knowledge proof is generated by this Python command.

The complete example is in [examples/response.json](examples/response.json). Floating-point last digits can vary across numeric environments.

### Explore through the local dashboard

```sh
python scripts/serve.py --port 8080
```

Open [http://127.0.0.1:8080](http://127.0.0.1:8080), select a workload and choose **Run and check**. The server listens on loopback and is intended for local inspection.

With the server running, a second terminal can call its workload inspection API:

```sh
curl "http://127.0.0.1:8080/api/run?id=valid-006-01"
```

This endpoint executes the bundled workload; it is not a production domain API.

## 6. Your Contributions / Research Alignment

### Implementation evidence

The following work areas are present in this reference and can be reviewed directly:

| Work area in this reference | Repository evidence |
| --- | --- |
| Eligibility policy reference | [src/syslab/credentials.py](src/syslab/credentials.py) |
| Correctness and edge cases | [tests/](tests/) and [acceptance workloads](workloads/) |
| Reproducible evaluation | [scripts/demo.py](scripts/demo.py), [scripts/benchmark.py](scripts/benchmark.py), [testing notes](docs/TESTING.md) |

### Research alignment

The project connects privacy-oriented application design, credential policy and cryptographic protocol implementation. Research discussion should distinguish what the application checks from what a validated proof system actually guarantees.

**A question to investigate:** How can freshness, expiry and verifier-context binding be validated end to end without exposing private credential attributes?

This question is a proposed extension, not a completed research result. Evaluate it with controlled inputs, independent correctness checks and measurements tied to a reproducible configuration.

### Personal contribution record

This reference was generated from the supplied project concept. Personal authorship or research contributions have not been verified. For an MS application, document only the modules you actually changed, the design choices you can explain, and experiments you ran; link those claims to commits or reproducible reports. See [Provenance](docs/PROVENANCE.md).

All bundled inputs are synthetic. The repository does not establish historical development dates, prior deployment or published research.
