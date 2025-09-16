// Optional actual Groth16 path; requires npm dependencies, Circom output and an audited zkey.
import fs from 'node:fs';
import crypto from 'node:crypto';
import * as snarkjs from 'snarkjs';
import {buildPoseidon,buildEddsa} from 'circomlibjs';
const args=process.argv.slice(2);
const stringify=value=>JSON.stringify(value,(_,v)=>typeof v==='bigint'?v.toString():v,2);
try {
  if(args[0]==='issue'){
    if(args.length!==5)throw new Error('issue credential-request.json issuer-private-key-hex.txt policy.json witness.json');
    const request=JSON.parse(fs.readFileSync(args[1],'utf8')),policy=JSON.parse(fs.readFileSync(args[3],'utf8'));
    const key=Buffer.from(fs.readFileSync(args[2],'utf8').trim(),'hex');if(key.length!==32)throw new Error('32-byte issuer key required');
    const poseidon=await buildPoseidon(),eddsa=await buildEddsa();
    const dob=BigInt(request.dob),expiry=BigInt(request.expiry),salt=BigInt('0x'+crypto.randomBytes(31).toString('hex'));
    const message=poseidon.F.toObject(poseidon([dob,expiry,salt]));
    const signature=eddsa.signPoseidon(key,eddsa.F.e(message)),pub=eddsa.prv2pub(key);
    const witness={dob,expiry,salt,commitment:message,R8x:eddsa.F.toObject(signature.R8[0]),R8y:eddsa.F.toObject(signature.R8[1]),S:signature.S,issuerAx:eddsa.F.toObject(pub[0]),issuerAy:eddsa.F.toObject(pub[1]),cutoff:policy.cutoff,now:policy.now,nonce:policy.nonce,audience:policy.audience};
    fs.writeFileSync(args[4],stringify(witness),{mode:0o600});
    console.log('Private witness written. Validate issuer public key against verifier policy.');
  }else if(args[0]==='prove'){
    if(args.length!==5)throw new Error('prove witness.json circuit.wasm circuit_final.zkey output-prefix');
    const witness=JSON.parse(fs.readFileSync(args[1],'utf8'));
    const {proof,publicSignals}=await snarkjs.groth16.fullProve(witness,args[2],args[3]);
    fs.writeFileSync(args[4]+'.proof.json',stringify(proof));fs.writeFileSync(args[4]+'.public.json',stringify(publicSignals));console.log('Groth16 proof generated.');
  }else throw new Error('use issue or prove command');
  process.exit(0);
}catch(error){console.error(error.message);process.exit(1);}
