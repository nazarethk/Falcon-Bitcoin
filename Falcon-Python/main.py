import falcon
from cryptos import Bitcoin , sha256, ripemd160
c = Bitcoin(testnet=False)

def printCredentials(name, sk, pk, address):
    print("###################")
    print(name, "credentials:")
    print("###################\n")
    print("Secret Vector:",sk.h)
    print("\nSecret Key:", sk.sha,"(",len(sk.sha)/2,"bytes)")
    print("\nPublic Key (uncompressed):" ,pk.hex, "(",len(pk.hex)/2,"bytes)\n")
    print("\nPublic Key Hash:" ,pk.sha, "(",len(pk.sha)/2,"bytes)\n")
    validity = "is valid" if c.is_p2sh(address) else "is not valid"
    print(name, "address:", address, validity)

def generateKeys():
    sk = falcon.SecretKey(256)
    sk.sha = sha256(sk.hex)
    pk = falcon.PublicKey(sk)
    pk.sha = sha256(pk.hex)
    address = c.pubtop2wpkh_p2sh(ripemd160(pk.sha)) # P2SH (BASE58) - Segwit - Pay to Script Hash
    return sk, pk ,address

Alice_SecretKey, Alice_PublicKey, Alice_address = generateKeys()
printCredentials("Alice", Alice_SecretKey, Alice_PublicKey, Alice_address)

Bob_SecretKey, Bob_PublicKey, Bob_address = generateKeys()
printCredentials("Bob", Bob_SecretKey, Bob_PublicKey, Bob_address)

message = "Bitcoin is great"
sig = Alice_SecretKey.sign(message.encode())

print("\nSignature is ", sig, "(",len(sig)/2,"bytes)")
verified = Alice_PublicKey.verify(message.encode(), sig)
print("Verified: ",verified)
