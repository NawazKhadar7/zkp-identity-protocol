import random,hmac,hashlib,datetime
from .common import validate_case,dumps
from .credentials import issue,evaluate
from .nonce import Nonces
FAMILIES=('valid','underage','bad-commitment','wrong-issuer','expired','replayed')
def day(year,month,day):return (datetime.date(year,month,day)-datetime.date(1970,1,1)).days
def run_case(case):
    validate_case(case)
    if case['family'] not in FAMILIES:raise ValueError('unknown identity family')
    family=case['family'];n=case['size'];key=b'synthetic-reference-key-not-for-production';ledger=Nonces();accepted=0;reasons=[];now=day(2026,10,1);cutoff=day(2005,10,1)
    for i in range(n):
        dob=day(2010,1,1) if family=='underage' else day(2000,1,1);expiry=now-1 if family=='expired' else now+30
        credential=issue(dob,expiry,str(case['seed'])+'-'+str(i),key,'other-issuer' if family=='wrong-issuer' else 'demo-issuer')
        if family=='bad-commitment':
            credential['payload']['commitment']='0'*64
            credential['mac']=hmac.new(key,dumps(credential['payload']).encode(),hashlib.sha256).hexdigest()
        nonce=f'n-{i}';valid,reason=evaluate(credential,key,'demo-issuer',cutoff,now)
        if family=='replayed':ledger.consume('reference-app',nonce)
        if valid and not ledger.consume('reference-app',nonce):valid=False;reason='replay'
        accepted+=valid;reasons.append(reason)
    return {'metrics':{'requests':n,'accepted_in_reference':accepted,'rejected':n-accepted,'is_cryptographic_proof':False,'replays_rejected':family!='replayed' or accepted==0},'output':{'mode':'plaintext policy evaluation; not zero-knowledge','reasons':reasons[:8]}}
