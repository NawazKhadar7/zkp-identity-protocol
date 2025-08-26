"""Reference credential policy evaluator. This module does NOT create a ZK proof."""
import hashlib,hmac
from .common import dumps

def commitment(dob,expiry,salt):return hashlib.sha256(dumps([dob,expiry,salt]).encode()).hexdigest()
def issue(dob,expiry,salt,key,issuer='demo-issuer'):
    payload={'dob':dob,'expiry':expiry,'salt':salt,'issuer':issuer,'commitment':commitment(dob,expiry,salt)}
    return {'payload':payload,'mac':hmac.new(key,dumps(payload).encode(),hashlib.sha256).hexdigest()}
def evaluate(credential,key,issuer,cutoff,now):
    p=credential['payload'];mac=hmac.new(key,dumps(p).encode(),hashlib.sha256).hexdigest()
    if not hmac.compare_digest(mac,credential['mac']):return False,'bad-mac'
    if p['issuer']!=issuer:return False,'untrusted-issuer'
    if commitment(p['dob'],p['expiry'],p['salt'])!=p['commitment']:return False,'bad-commitment'
    if not 0<=p['dob']<=cutoff:return False,'under-threshold'
    if p['expiry']<now:return False,'expired'
    return True,'policy-satisfied'
