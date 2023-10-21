import falcon
from cryptos import Bitcoin , sha256
c = Bitcoin(testnet=True)
def generateKeys():
    sk = falcon.SecretKey(256)
    pk = falcon.PublicKey(sk)
    sk.sha = sha256(sk.hex)
    pk.hex = c.privtopub(sk.sha)
    pk.h = [int(x) for x in bytes.fromhex(pk.hex)]
    address = c.privtoaddr(sk.sha)
    return sk, pk ,address

Alice_SecretKey, Alice_PublicKey, Alice_address = generateKeys()
print("###################\nAlice credentials:\n###################\nSecret Vector:",Alice_SecretKey.h,"\n\nSecret Key:", Alice_SecretKey.sha, "(",len(Alice_SecretKey.sha)/2,"bytes)\n\nPublic Key (uncompressed):" ,Alice_PublicKey.hex,  "(",len(Alice_PublicKey.hex)/2,"bytes)\n\nAlice address:", Alice_address)

Bob_SecretKey, Bob_PublicKey, Bob_address = generateKeys()

print("\n###################\nBob credentials:\n###################\nSecret Vector:",Bob_SecretKey.h,"\n\nSecret Key:", Bob_SecretKey.sha, "(",len(Bob_SecretKey.sha)/2,"bytes)\n\nPublic Key (uncompressed):" ,Bob_PublicKey.hex,"(",len(Bob_PublicKey.hex)/2,"bytes)\n\nBob address:",Bob_address)
message = "Bitcoin is great"
sig = Alice_SecretKey.sign(message.encode())

print("\nSignature is ", sig, "(",len(sig)/2,"bytes)")
verified = Alice_PublicKey.verify(message.encode(), sig)
print("Verified: ",verified)

