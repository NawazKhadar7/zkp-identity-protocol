class Nonces:
    def __init__(self):self.used=set()
    def consume(self,audience,nonce):
        if not isinstance(audience,str) or not audience or not isinstance(nonce,str) or not nonce:raise ValueError('nonempty audience and nonce required')
        key=(audience,nonce)
        if key in self.used:return False
        self.used.add(key);return True
