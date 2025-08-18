#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")/.."
mkdir -p artifacts/circuit
command -v circom >/dev/null 2>&1 || { echo "Circom 2 is required" >&2; exit 1; }
circom circuits/credential.circom --r1cs --wasm --sym -o artifacts/circuit
