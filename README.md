# Bitcoin Core with Falcon: Post-Quantum Security

🔒 This repository aims to enhance the security of Bitcoin Core by integrating the Falcon lattice-based digital signature algorithm into the Bitcoin Core. Falcon is designed to provide post-quantum security, safeguarding the Bitcoin network against potential quantum computing threats. [See Example](#code-testnetpy)

## About Falcon

Falcon is a cryptographic signature algorithm submitted to the NIST Post-Quantum Cryptography Project. It is designed to resist attacks from quantum computers, making it a promising choice for securing Bitcoin transactions in a post-quantum era.

Key features of Falcon include:

- **Security**: Falcon is based on the theoretical framework of Gentry, Peikert, and Vaikuntanathan for lattice-based signature schemes, providing robust security.
- **Compactness**: Falcon signatures are substantially shorter than many other lattice-based signature schemes, making them efficient for blockchain use.
- **Speed**: Implementation of fast Fourier sampling allows for rapid signature creation and verification.
- **Scalability**: Falcon offers efficient operations, allowing for long-term security parameters at a moderate cost.
- **RAM Economy**: Enhanced key generation in Falcon uses minimal RAM, making it compatible with memory-constrained devices.

## Performance

Falcon's performance on a common desktop computer is impressive:

- **Falcon-512**: Key generation time: 8.64 ms, Signature generation speed: 5948.1 signatures per second, Public key size: 897 bytes, Signature size: 666 bytes.
- **Falcon-1024**: Key generation time: 27.45 ms, Signature generation speed: 2913.0 signatures per second, Public key size: 1793 bytes, Signature size: 1280 bytes.

These performance metrics demonstrate Falcon's efficiency and suitability for real-world applications.

## Usage

This project includes two Python scripts, `main.py` and `testnet.py` in `Falcoin-Python` folder, for working with Bitcoin-related operations and cryptography. Below, you'll find short descriptions of each file, along with links to detailed explanations.

### `main.py`

[Detailed Explanation](#detailed-explanation-mainpy)

`main.py` is a Python script that demonstrates how to generate Bitcoin key pairs, create addresses, and perform digital signatures for transactions, using Falcon lattice-based cryptography.

### `testnet.py`

[Detailed Explanation](#detailed-explanation-testnetpy)

`testnet.py` is a Python script that showcases Bitcoin-related operations within the Bitcoin testnet environment. It covers key generation, UTXO retrieval, transaction signing, and broadcasting. This script is a valuable tool for simulating Bitcoin transactions without using real Bitcoin, using the Falcon generated key pairs and addresses.

## Detailed Explanation: `main.py`

### Overview

### Steps in the Code

1. **Import Libraries**: Import the necessary libraries for Bitcoin-related operations and cryptography.

2. **Generate Keys**: A function is defined to generate cryptographic key pairs and Bitcoin addresses.

3. **Generate Alice's Keys**: Generate key pairs and an address for Alice.

4. **Generate Bob's Keys**: Generate key pairs and an address for Bob.

5. **Message Signing**: A message is signed using Alice's secret key.

6. **Signature Verification**: Verify the signed message using Alice's public key.
7. 
<a name="code-testnetpy"></a>
### Code

```
import falcon
from cryptos import Bitcoin , sha256
c = Bitcoin(testnet=True)
def generateKeys():
    sk = falcon.SecretKey(256) # or using 8 and enabling pkGeneration
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
```

## Detailed Explanation: `testnet.py`

### Overview

`testnet.py` is a Python script for simulating Bitcoin transactions within the Bitcoin testnet environment. It covers key pair generation, unspent transaction output retrieval, transaction signing, and broadcasting.

### Steps in the Code

1. **Import Libraries**: Import the necessary libraries for Bitcoin-related operations.

2. **Initialize Bitcoin Testnet**: Create a Bitcoin testnet instance.

3. **Define Alice's and Bob's Credentials**: Define cryptographic credentials for both Alice and Bob (hardcoded), generated by `main.py`

4. **Retrieve UTXOs**: Fetch the unspent transaction outputs (UTXOs) associated with Bob's Bitcoin address on the testnet.

5. **Create and Sign Transaction**: Create a Bitcoin transaction from Bob to Alice and sign it using Bob's secret key.

6. **Serialize and Broadcast Transaction**: Serialize the transaction data and push it to the testnet. Print the signature and transaction result.

### Code

```
from cryptos import Bitcoin, serialize
c = Bitcoin(testnet=True)

Alice_SecretKey = "fa72ef16262777b0b1c3c9fd938983c6cbab46e3884394a1a54e38cca7a33200"
Alice_PublicKey = "0462952e1e351896d0dfcbcb147e50e7a5355f2f8fded563d1721f4c462479cd63e284b9f165b43902c473fbf26667ff656fcbf87d4de68b178f15ea71f59f5bc3"
Alice_address = "mveYRKd8UZKUmb5AWBufyGyQ11CriakgwQ"
print("###################\nAlice credentials:\n###################\nSecret Vector:",Alice_SecretKey,"\n\nSecret Key:", Alice_SecretKey, "(",len(Alice_SecretKey)/2,"bytes)\n\nPublic Key (uncompressed):" ,Alice_PublicKey,  "(",len(Alice_PublicKey)/2,"bytes)\n\nAlice address:", Alice_address)

Bob_SecretKey = "a7ed1259963d4be24d5c4d3ebe40c7a6548e1c9b9d402ebf9498bdf3d64cc239"
Bob_PublicKey = "04e760db9f177d6d776c84f8f3dd330dd7d87c93f1a98092fb403c04bb1b0f52a429bb4ba8c9f00524c4764739a74e00acb3c6c6b23a1ebd3d316852f3e6a5089e"
Bob_address = "mywrcLXoaifhjdPNtaUCkezd54yWVNS4db"

print("\n###################\nBob credentials:\n###################\nSecret Vector:",Bob_SecretKey,"\n\nSecret Key:", Bob_SecretKey, "(",len(Bob_SecretKey)/2,"bytes)\n\nPublic Key (uncompressed):" ,Bob_PublicKey,"(",len(Bob_PublicKey)/2,"bytes)\n\nBob address:",Bob_address)
# Fetch the sender's unspent transaction outputs (UTXOs)
sender_utxos = c.unspent(Bob_address)
print(sender_utxos)

# Create a transaction input from one of the sender's UTXOs
txin = sender_utxos[0]
tx = c.preparesignedtx(Bob_SecretKey, Bob_address, Alice_address, 100)
sig = serialize(tx)
res = c.pushtx(tx)
print("signature:", sig)
print("result:", res)
```

### Output

```
###################
Alice credentials:
###################
Secret Vector: [10929, 4547, 1475, 10943, 2461, 202, 2648, 5145, 4693, 9249, 7348, 4620, 6476, 10001, 6370, 10716, 3460, 10231, 4149, 2020, 3850, 5646, 11009, 12032, 11610, 5747, 11500, 6481, 5450, 8069, 11469, 5515, 1344, 8106, 8845, 8048, 6711, 9369, 2007, 10476, 1623, 9390, 559, 6443, 6485, 9473, 3634, 2586, 5483, 1691, 9848, 362, 6953, 1562, 7502, 2027, 5087, 11996, 506, 6001, 7078, 9079, 3083, 6026, 11420, 10326, 1175, 9070, 6972, 11949, 8757, 11698, 4085, 11119, 10865, 4393, 2540, 8652, 10336, 2295, 7619, 8813, 8100, 9676, 2620, 11465, 894, 10479, 6222, 8213, 3377, 11994, 9898, 7334, 748, 2703, 6462, 4573, 5169, 10007, 9183, 12048, 5814, 1170, 4630, 2476, 9730, 2715, 165, 9000, 1504, 3871, 10297, 547, 10776, 10353, 1302, 106, 8238, 7052, 7173, 11493, 246, 5166, 11410, 4889, 839, 11471, 8637, 11046, 4058, 3518, 1273, 2341, 10663, 11306, 8299, 2045, 10330, 6242, 10000, 340, 5933, 1287, 7711, 11703, 12202, 10169, 10660, 7904, 566, 4073, 8924, 10618, 2337, 9947, 917, 4930, 5480, 5475, 270, 5979, 1663, 365, 10784, 5864, 3991, 7964, 9973, 1343, 712, 6737, 10293, 5686, 1574, 6753, 4075, 2751, 9136, 5410, 11284, 8547, 7243, 11975, 10158, 10636, 1714, 509, 8573, 8527, 9018, 10188, 11291, 9775, 1893, 9876, 11148, 3895, 8936, 9734, 12022, 10976, 5535, 5732, 12261, 5541, 7205, 3973, 10535, 7709, 4961, 7037, 5401, 5813, 2965, 6363, 10911, 9242, 8712, 9321, 547, 3663, 734, 1729, 10741, 10967, 3086, 4062, 7919, 9681, 10013, 8389, 3280, 12141, 532, 9445, 10967, 1645, 9278, 7861, 2496, 11360, 2357, 9460, 12017, 9177, 11638, 6334, 4560, 873, 342, 855, 5748, 3973, 3274, 325] 

Secret Key: fa72ef16262777b0b1c3c9fd938983c6cbab46e3884394a1a54e38cca7a33200 ( 32.0 bytes)

Public Key (uncompressed): 0462952e1e351896d0dfcbcb147e50e7a5355f2f8fded563d1721f4c462479cd63e284b9f165b43902c473fbf26667ff656fcbf87d4de68b178f15ea71f59f5bc3 ( 65.0 bytes)

Alice address: mveYRKd8UZKUmb5AWBufyGyQ11CriakgwQ

###################
Bob credentials:
###################
Secret Vector: [5693, 11638, 3349, 2952, 1705, 8054, 3279, 3037, 4465, 8425, 156, 332, 4680, 3572, 6651, 5012, 7887, 3670, 10021, 525, 5859, 4839, 8480, 2859, 2265, 3537, 23, 12015, 2512, 5532, 5401, 11082, 11372, 9804, 10833, 5332, 2303, 2166, 4082, 7239, 8191, 5681, 2077, 7999, 8327, 11708, 5638, 1646, 7023, 916, 11092, 9797, 12255, 7764, 11497, 2876, 10900, 5508, 1887, 3458, 5973, 6774, 7629, 1753, 5624, 1048, 9014, 2439, 502, 2544, 8102, 7904, 4554, 758, 5744, 6583, 7515, 10456, 7319, 4906, 5686, 6449, 6140, 6301, 5355, 8070, 2216, 5893, 2849, 4872, 11593, 10731, 10297, 2453, 7710, 4860, 9410, 6968, 8352, 2521, 4772, 8280, 11099, 7522, 4763, 11334, 3028, 6860, 7379, 11369, 9146, 11345, 8474, 10957, 1616, 6669, 693, 3832, 7258, 5938, 1776, 3286, 2015, 9963, 350, 10466, 6185, 12231, 4094, 1854, 10653, 10446, 11532, 1109, 29, 4320, 5392, 11215, 8981, 5146, 5201, 10488, 11563, 8470, 4049, 9569, 6025, 8820, 2312, 5744, 1227, 9911, 10152, 2343, 10161, 4421, 10761, 9215, 4313, 9102, 2662, 256, 5528, 263, 7528, 8261, 2682, 6253, 64, 1425, 6060, 5298, 8962, 74, 2142, 10812, 475, 70, 591, 11309, 9679, 2198, 6996, 10969, 2230, 9116, 6660, 4760, 1752, 8023, 1871, 10671, 7211, 6921, 10230, 5811, 2870, 11427, 1536, 5908, 7117, 5671, 10223, 11977, 2337, 8771, 5434, 1792, 7143, 11080, 9813, 4250, 10371, 4644, 2369, 9610, 4919, 4817, 9151, 2708, 5742, 9326, 8184, 8088, 3061, 11553, 5557, 1986, 9807, 10579, 10013, 7456, 9281, 4222, 3688, 2369, 4240, 10666, 2943, 3572, 12249, 1001, 3879, 313, 10924, 11538, 1321, 7202, 4904, 9086, 2127, 4771, 4977, 6301, 7213, 11466] 

Secret Key: a7ed1259963d4be24d5c4d3ebe40c7a6548e1c9b9d402ebf9498bdf3d64cc239 ( 32.0 bytes)

Public Key (uncompressed): 04e760db9f177d6d776c84f8f3dd330dd7d87c93f1a98092fb403c04bb1b0f52a429bb4ba8c9f00524c4764739a74e00acb3c6c6b23a1ebd3d316852f3e6a5089e ( 65.0 bytes)

Bob address: mywrcLXoaifhjdPNtaUCkezd54yWVNS4db
[{'tx_hash': '0966056529ddc4e8415a4ba0417ea94bae570d84ee04ea27f52a966aff77ffb7', 'tx_pos': 1, 'height': 0, 'value': 7149, 'address': 'mywrcLXoaifhjdPNtaUCkezd54yWVNS4db'}]
signature: 0100000001b7ff77ff6a962af527ea04ee840d57ae4ba97e41a04b5a41e8c4dd2965056609010000008a47304402204bc2299696c0e544f5f7d2b5d103c21aedf739a07751cc35866ea7dc8cf25e3f022069dafa00be8e85b957abbb79c80884d6a8bdd93a210e1376a0708d06d224b8c2014104e760db9f177d6d776c84f8f3dd330dd7d87c93f1a98092fb403c04bb1b0f52a429bb4ba8c9f00524c4764739a74e00acb3c6c6b23a1ebd3d316852f3e6a5089effffffff0264000000000000001976a914a5f948ecb6f29821aebcc1ea80f4319463f8f35f88aca1170000000000001976a914ca27eaf191f26bbf05987acda5ffea19aa3d669788ac00000000
result: 426f81493767fad18b4bc945ac06a3f7c9e8269359ce2043378e0ff44b97bfb8
```

## Additional Contents

- [Falcon Specification (PDF)](https://falcon-sign.info/falcon.pdf)
- [Falcon Website](https://falcon-sign.info/)
- [pybitcointools](https://github.com/primal100/pybitcointools)
- [falcon.py](https://github.com/tprest/falcon.py)
