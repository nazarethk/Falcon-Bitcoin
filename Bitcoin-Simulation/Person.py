import falcon
from cryptos import sha256, ripemd160, bin_to_b58check

class Person:
    def __init__(self, n):
        self.sk = falcon.SecretKey(n)
        self.pk = falcon.PublicKey(self.sk)
        self.wallet_address = bin_to_b58check(bytes.fromhex((ripemd160(sha256(self.pk.hex)))))
        self.utxos = []

    def calculate_hash160(self):
        pubkey_hex = self.pk.hex
        hash160 = ripemd160(sha256(pubkey_hex))
        return hash160

    def calculate_scriptSig(self, json_bytes):
        signature = self.sk.sign(json_bytes)
        pubkey_hex = self.pk.hex
        scriptSig = str(len(signature)) + signature + str(len(pubkey_hex)) + pubkey_hex
        return scriptSig

    def calculate_scriptPubKey(self):
        hash160 = self.calculate_hash160()
        scriptPubKey = "76a9" + str(len(hash160)) + hash160 + "88ac"
        return scriptPubKey

