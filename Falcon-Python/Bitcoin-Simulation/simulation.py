import json
import sys
sys.path.append("..")  
from Person import Person  # Assuming the Person class is defined in person.py
from BitcoinWrapper import verify
from cryptos import sha256


# Create instances for Alice and Bob
alice = Person()
bob = Person()

# Print Alice's data
print("\nAlice's credentials:\n")
print("\nAlice's Secret Key:", alice.sk)
print("\nAlice's Public Key:", alice.pk.hex)
print("\nAlice's Hash160:", alice.calculate_hash160())
print("\nAlice's ScriptSig:", alice.calculate_scriptSig(b"Hello"))
print("\nAlice's Address:", alice.wallet_address)


# Print Bob's data
print("\nBob's credentials:\n")
print("\nBob's Secret Key:", bob.sk)
print("\nBob's Public Key:", bob.pk.hex)
print("\nBob's Hash160:", bob.calculate_hash160())
print("\nBob's ScriptSig:", bob.calculate_scriptSig(b"Hi"))
print("\nBob's ScriptPubKey:", bob.calculate_scriptPubKey())
print("\nBob's Address:", bob.wallet_address, "\n")

# Let's assume Alice was the first person to have bitcoin, and she received the first mining reward of 50 BTC
alice.utxos = [
    {
      "tx_hash": "d3ed3aa3fd979622858d0dce1c98cfee3468741a851b20ed2159558df935d22d",
      "vout": 0,
      "sequence": 123456789,
      "value": 5000000000,
      "ScriptPubKey": alice.calculate_scriptPubKey()
    }
]

# Now let's say that we want alice to send 1 BTC to Bob

# 1. Let's prepare the tranasction json

tx = {
  "version": 1,
  "inputs": [
    {
      "tx_hash": "d3ed3aa3fd979622858d0dce1c98cfee3468741a851b20ed2159558df935d22d",
      "vout": 0,
      "scriptSig": "", # We will populate with Alice's scriptSig
      "sequence": 123456789
    }
  ],
  "outputs": [
    {
      "value": 100000000,
      "scriptPubKey":  bob.calculate_scriptPubKey() # We will populate with Bob's scriptPubKey
    },
    {
      "value": 490000000,
      "scriptPubKey": alice.calculate_scriptPubKey() # We will populate with Alice's scriptPubKey, to send back the 49 BTC as a UTXO
    }
    ],
  "locktime": 0
}

# 2. Sign the transaction using Alice's private key
json_bytes = json.dumps(tx).encode('utf-8')
aliceScriptSig = alice.calculate_scriptSig(json_bytes)
tx["inputs"][0]["scriptSig"] = aliceScriptSig
print(tx)

# Now we have the transaction ready to be broadcasted and verified. 
# For educational purposes we will verify using our code, instead of a testnet.

# 3. Verify the transaction
if verify(aliceScriptSig,json_bytes):
    print("Validated!")
    bob_utxo = {
      "tx_hash": sha256(sha256(json.dumps(tx).encode('utf-8'))),
      "vout": 0,
      "sequence": 123456789,
      "value": 100000000,
      "ScriptPubKey": bob.calculate_scriptPubKey()
    }
    bob.utxos.append(bob_utxo)
    print("Bob's utxos:", bob.utxos)
    print(bob.utxos)
    # As alice spent the utxo and had only one, we ovveride the utxo with the following
    alice.utxos = [
      {
        "tx_hash": sha256(sha256(json.dumps(tx).encode('utf-8'))),
        "vout": 0,
        "sequence": 123456789,
        "value": 4900000000,
        "ScriptPubKey": alice.calculate_scriptPubKey()
      }
    ]
    print("Alice's utxos:", alice.utxos)
    
else:
    print("The signature is not valid (OP_CHECKSIG failed)")


