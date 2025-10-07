// Single-process file-ledger demo. A concurrent service needs transactional nonce storage.
import fs from 'node:fs';
import * as snarkjs from 'snarkjs';
const args=process.argv.slice(2);
try{
  if(args.length!==5)throw new Error('verification_key.json public.json proof.json trusted-policy.json nonce-ledger.json');
  const [vkey,signals,proof,policy]=args.slice(0,4).map(p=>JSON.parse(fs.readFileSync(p,'utf8')));
  const names=['issuerAx','issuerAy','cutoff','now','nonce','audience'];
  if(signals.length!==7||names.some((name,i)=>String(policy[name])!==String(signals[i+1])))throw new Error('public signals differ from trusted policy');
  const key=String(policy.audience)+':'+String(policy.nonce),ledger=fs.existsSync(args[4])?JSON.parse(fs.readFileSync(args[4],'utf8')):[];
  if(!Array.isArray(ledger)||ledger.includes(key))throw new Error('nonce already used or ledger invalid');
  if(!await snarkjs.groth16.verify(vkey,signals,proof))throw new Error('invalid Groth16 proof');
  ledger.push(key);fs.writeFileSync(args[4]+'.tmp',JSON.stringify(ledger),{mode:0o600});fs.renameSync(args[4]+'.tmp',args[4]);
  console.log(JSON.stringify({cryptographic_proof_verified:true,challenge_consumed:true}));process.exit(0);
}catch(error){console.error(error.message);process.exit(1);}
