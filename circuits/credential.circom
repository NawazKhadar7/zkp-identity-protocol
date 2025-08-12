pragma circom 2.1.6;
include "../node_modules/circomlib/circuits/poseidon.circom";
include "../node_modules/circomlib/circuits/eddsaposeidon.circom";
include "../node_modules/circomlib/circuits/comparators.circom";
include "../node_modules/circomlib/circuits/bitify.circom";

template Credential(){
    signal input dob;
    signal input expiry;
    signal input salt;
    signal input commitment;
    signal input R8x;
    signal input R8y;
    signal input S;
    signal input issuerAx;
    signal input issuerAy;
    signal input cutoff;
    signal input now;
    signal input nonce;
    signal input audience;
    signal output nullifier;
    component dobBits=Num2Bits(32);dobBits.in <== dob;
    component expiryBits=Num2Bits(32);expiryBits.in <== expiry;
    component cutoffBits=Num2Bits(32);cutoffBits.in <== cutoff;
    component nowBits=Num2Bits(32);nowBits.in <== now;
    component digest=Poseidon(3);
    digest.inputs[0] <== dob;digest.inputs[1] <== expiry;digest.inputs[2] <== salt;
    digest.out === commitment;
    component signature=EdDSAPoseidonVerifier();
    signature.enabled <== 1;signature.Ax <== issuerAx;signature.Ay <== issuerAy;
    signature.R8x <== R8x;signature.R8y <== R8y;signature.S <== S;signature.M <== commitment;
    component age=LessEqThan(32);age.in[0] <== dob;age.in[1] <== cutoff;age.out === 1;
    component valid=LessEqThan(32);valid.in[0] <== now;valid.in[1] <== expiry;valid.out === 1;
    component challenge=Poseidon(3);challenge.inputs[0] <== salt;challenge.inputs[1] <== nonce;challenge.inputs[2] <== audience;
    nullifier <== challenge.out;
}
component main {public [issuerAx,issuerAy,cutoff,now,nonce,audience]}=Credential();
