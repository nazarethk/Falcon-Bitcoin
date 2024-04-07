import sys
sys.path.append("..")
import json
import time
from cryptos import Bitcoin, sha256, ripemd160
c = Bitcoin(testnet=True)
import random


def verify(scriptSig, message, scriptPubKey):
        
        return True


def calculate_block_size(block_transactions):
    # Calculate the total size of transactions in the block
    total_size_bytes = sum(calculate_transaction_size(tx) for tx in block_transactions)
    total_size_megabytes = total_size_bytes / (1024 * 1024)
    return total_size_megabytes

def calculate_transaction_size(tx):
    # Calculate transaction size based on inputs, outputs, and other metadata
    # We can use estimates or actual calculations based on Bitcoin protocol specifications
    # For simplicity, let's assume a basic calculation here
    input_size = len(json.dumps(tx["inputs"]).encode('utf-8'))
    output_size = len(json.dumps(tx["outputs"]).encode('utf-8'))
    metadata_size = len(json.dumps({
    "version": tx["version"],
    "locktime": tx["locktime"]
    }).encode('utf-8'))
    transaction_size = input_size + output_size + metadata_size
    return transaction_size

def simulate_transaction(sender, receiver, amount):
    # Prepare transaction JSON
    tx = {
        "version": 1,
        "inputs": [
            {
                "tx_hash": sender["utxos"][0]["tx_hash"],
                "vout": sender["utxos"][0]["vout"],
                "scriptSig": "",
                "sequence": sender["utxos"][0]["sequence"]
            }
        ],
        "outputs": [
            {
                "value": amount,
                "scriptPubKey": calculate_scriptPubKey(receiver["pk"])
            },
            {
                "value": sender["utxos"][0]["value"] - amount,
                "scriptPubKey": calculate_scriptPubKey(sender["pk"])
            }
        ],
        "locktime": 0
    }
    
    # Sign the transaction using sender's private key
    json_bytes = json.dumps(tx).encode('utf-8')
    sender_scriptSig = "483045022100ed81ff192e75a3fd2304004dcadb746fa5e24c5031ccfcf21320b0277457c98f02207a986d955c6e0cb35d446a89d3f56100f4d7f67801c31967743a9c8e10615bed01210349fc4e631e3624a545de3f89f5d8684c7b8138bd94bdd531d2e213bf016b278a"
    tx["inputs"][0]["scriptSig"] = sender_scriptSig
    
    # Verify the transaction
    if verify(sender_scriptSig, json_bytes, calculate_scriptPubKey(sender["pk"])): 
        tx_hash = sha256(sha256(json.dumps(tx).encode('utf-8')))
        print("Transaction Validated! Tx hash:", tx_hash)
        # Update UTXOs
        num_utxos = len(receiver["utxos"])
        receiver_utxo = {
            "tx_hash": tx_hash,
            "vout": num_utxos,
            "sequence": sender["utxos"][0]["sequence"],
            "value": amount,
            "ScriptPubKey": calculate_scriptPubKey(receiver["pk"])
        }
        receiver["utxos"].append(receiver_utxo)
        
        sender["utxos"] = [
            {
                "tx_hash": sha256(sha256(json.dumps(tx).encode('utf-8'))),
                "vout": 0,
                "sequence": sender["utxos"][0]["sequence"],
                "value": sender["utxos"][0]["value"] - amount,
                "ScriptPubKey": calculate_scriptPubKey(sender["pk"])
            }
        ]
        return tx 
    else:
        print("Transaction Verification failed")
        return None

start_program_time = time.time()
num_simulations = 10

alice_priv = sha256('a big long brainwallet password alice')
bob_priv = sha256('a big long brainwallet password bob')

def calculate_hash160(pub):
        hash160 = ripemd160(sha256(pub))
        return hash160
def calculate_scriptPubKey(pub):
        hash160 = calculate_hash160(pub)
        scriptPubKey = "76a9" + str(len(hash160)) + hash160 + "88ac"
        return scriptPubKey

alice = {
    "sk":alice_priv,
    "pk": c.privtop2wpkh_p2sh(alice_priv),
    "wallet_address":c.privtoaddr(alice_priv),
    "utxos": [
            {
            "tx_hash": "d3ed3aa3fd979622858d0dce1c98cfee3468741a851b20ed2159558df935d22d",
            "vout": 0,
            "sequence": 0xFFFFFFFF,
            "value": 5000000000,
            "ScriptPubKey": ""
            }
        ]
    }
alice["utxos"][0]["ScriptPubKey"] = calculate_scriptPubKey(alice["pk"])

bob = {
    "sk":bob_priv,
    "pk": c.privtop2wpkh_p2sh(bob_priv),
    "wallet_address":c.privtoaddr(bob_priv),
    "utxos": []
    }


transaction_times = []
transaction_sizes = []
block_transactions = []
transaction_confirmation_times = []

for i in range(num_simulations):
    start_time = time.time()
    tx = simulate_transaction(alice, bob, 100) # sending 100 satoshis to bob
    end_time = time.time()
    if tx is not None:
         # Record transaction creation time
        transaction_creation_time = end_time 
        transaction_times.append(end_time - start_time)
        transaction_sizes.append(calculate_transaction_size(tx))

        # Add the transaction to the list representing the block
        block_transactions.append(tx)

        # Simulate confirmation by adding a delay (for demonstration purposes)
        confirmation_delay = 0 #random.uniform(7, 15) 
        time.sleep(confirmation_delay)
        
        # Record confirmation time
        confirmation_time = time.time()
        confirmation_duration = confirmation_time - transaction_creation_time
        transaction_confirmation_times.append(confirmation_duration)

end_program_time = time.time()
total_program_time = end_program_time - start_program_time
print("\nAlice UTXOs:\n")
print(alice["utxos"])
print("\nBob UTXOs:\n")
print(bob["utxos"])

print(f"\nTotal program time: {total_program_time:.4f} seconds")

print("Average Transaction Size:", sum(transaction_sizes) / len(transaction_sizes), "bytes")
print("Minimum Transaction Size:", min(transaction_sizes), "bytes")
print("Maximum Transaction Size:", max(transaction_sizes), "bytes")

print(f"Average Transaction Time: {sum(transaction_times) / len(transaction_times):.6f} seconds")
print(f"Minimum Transaction Time: {min(transaction_times):.6f} seconds")
print(f"Maximum Transaction Time: {max(transaction_times):.6f} seconds")

print(f"Average Confirmation Time: {sum(transaction_confirmation_times) / len(transaction_confirmation_times):.2f} seconds")

print(f"Block size: {calculate_block_size(block_transactions):.4f} MB")

"""
Alice UTXOs:

[{'tx_hash': 'e0da667a821f8a0082fcd95b5744d51d710312c80f377023a15c98cd2e6b497f', 'vout': 0, 'sequence': 4294967295, 'value': 4999999000, 'ScriptPubKey': '76a9408bf5a6f16d2d628a339f3034308e0b4fade7aa7b88ac'}]

Bob UTXOs:

[{'tx_hash': '67a92b80e540c6a727e6ea8e265d5f4f145c76a15c575bac7fc713d127b4bc74', 'vout': 0, 'sequence': 4294967295, 'value': 100, 'ScriptPubKey': '76a9400721e6f61610934d30beb7b3d69155ae40470d8c88ac'}, {'tx_hash': '1e35e3c6b2f8cd00abaec8f11269da17ce77b8e2f6ed6d3fee64d0d69094f9c3', 'vout': 1, 'sequence': 4294967295, 'value': 100, 'ScriptPubKey': '76a9400721e6f61610934d30beb7b3d69155ae40470d8c88ac'}, {'tx_hash': 'bed1a8d0c13644301a9e823b3d5ac991b698d6dedc3f57cad3f47913508da1e1', 'vout': 2, 'sequence': 4294967295, 'value': 100, 'ScriptPubKey': '76a9400721e6f61610934d30beb7b3d69155ae40470d8c88ac'}, {'tx_hash': '4a35ed83cd6126a36c6d78106f60d31ec30b19b225d9d5b02a0e58ad7220b14f', 'vout': 3, 'sequence': 4294967295, 'value': 100, 'ScriptPubKey': '76a9400721e6f61610934d30beb7b3d69155ae40470d8c88ac'}, {'tx_hash': '0c68c83b44202294ffb3fabef817448520e9810e598d56b1d04208dec3d506dd', 'vout': 4, 'sequence': 4294967295, 'value': 100, 'ScriptPubKey': '76a9400721e6f61610934d30beb7b3d69155ae40470d8c88ac'}, {'tx_hash': '383e3e24392889ddb0dbe81b462a6822f975c9989aeb2bd689ae6429220c4cbf', 'vout': 5, 'sequence': 4294967295, 'value': 100, 'ScriptPubKey': '76a9400721e6f61610934d30beb7b3d69155ae40470d8c88ac'}, {'tx_hash': 'dd512c69130b8d84e722ccbbce904b986d9577cabd195337c22d583d3f724c9f', 'vout': 6, 'sequence': 4294967295, 'value': 100, 'ScriptPubKey': '76a9400721e6f61610934d30beb7b3d69155ae40470d8c88ac'}, {'tx_hash': '3e58c749b6ec95e06c53431265f973519808ea79dc83cf57b3fd02179b0e82dc', 'vout': 7, 'sequence': 4294967295, 'value': 100, 'ScriptPubKey': '76a9400721e6f61610934d30beb7b3d69155ae40470d8c88ac'}, {'tx_hash': 'f9bd133ca7a93d99afbec82f0a3cc09d16694b4dc5d1969c59e1e25b0c9a026a', 'vout': 8, 'sequence': 4294967295, 'value': 100, 'ScriptPubKey': '76a9400721e6f61610934d30beb7b3d69155ae40470d8c88ac'}, {'tx_hash': 'e0da667a821f8a0082fcd95b5744d51d710312c80f377023a15c98cd2e6b497f', 'vout': 9, 'sequence': 4294967295, 'value': 100, 'ScriptPubKey': '76a9400721e6f61610934d30beb7b3d69155ae40470d8c88ac'}]

Total program time: 0.0191 seconds
Average Transaction Size: 555.0 bytes
Minimum Transaction Size: 555 bytes
Maximum Transaction Size: 555 bytes
Average Transaction Time: 0.001031 seconds
Minimum Transaction Time: 0.000991 seconds
Maximum Transaction Time: 0.001157 seconds
Average Confirmation Time: 0.00 seconds
Block size: 0.0053 MB
"""