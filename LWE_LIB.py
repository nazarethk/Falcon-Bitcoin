"""
# This file contains multiple util functions, that are needed during the lattice based encryption process.
# Functions:
    - stringToBinary, transforms the string into a binary format (char)
    - binaryToString, transforms the binary format (char) into a string
    - generatePublicKey, generates a 33 byte hexadecimal public key from two public vectors A and B
    - generatePrivateKey, generates a 32 byte hexadecimal private key from two public vectors S1 and S2
    - ripemd160, it is used to hash the public key to get a 160-bit wallet address
    - generateWalletAddress, it is used to add the byte prefix into the output of ripemd160, computing the checksum, and converting into base58 bitcoin wallet address
    - generateKeys, generates A, B, s, e, secret_vector, secret_vector1 variables
    - encyrpt, encrypts the message with the two public vectors A and B
    - decrypt, decrypts the encrypted tuple (u,v) with the secret key s (which is the sum of the values of both vectors secret_vector and secret_vector1)
"""
import math
import random
import hashlib
import base58

def stringToBinary(input_string):
    binary_string = ''.join(format(ord(char), '08b') for char in input_string)
    return binary_string

def binaryToString(binary_string):
    byte_array = [int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8)]
    return ''.join(chr(byte) for byte in byte_array)

def generatePublicKey(A, B):
    # Ensure the values in A and B are within the valid byte range (0-255)
    A = [x % 256 for x in A]
    B = [x % 256 for x in B]

    # Convert vectors A and B to bytes
    public_key_bytes = bytes(A+B)

    # Convert the public key bytes to hexadecimal with 64 characters
    hexadecimal_public_key = public_key_bytes.hex()

    return "00"+hexadecimal_public_key

def generatePrivateKey(S1,S2):
    # Ensure the values in A and B are within the valid byte range (0-255)
    A = [x % 256 for x in S1]
    B = [x % 256 for x in S2]

    # Convert vectors A and B to bytes
    public_key_bytes = bytes(A+B)

    # Convert the public key bytes to hexadecimal with 64 characters
    hexadecimal_public_key = public_key_bytes.hex()

    return hexadecimal_public_key

def ripemd160(data):
    # Simulate the RIPEMD-160 hash (in reality, use a proper library)
    sha256_hash = hashlib.sha256(data.encode('utf-8'))
    ripemd160_hash = hashlib.new('ripemd160')
    ripemd160_hash.update(sha256_hash.digest())
    return ripemd160_hash.digest()

def generateWalletAddress(public_key):
    version_byte = b'\x00'  # Assuming you want "0x00" as the version byte
    ripemd_160 = ripemd160(public_key)
    checksum = hashlib.sha256(hashlib.sha256(version_byte + ripemd_160).digest()).digest()[:4]
    hash_bytes = version_byte + ripemd_160 + checksum
    wallet_address = base58.b58encode(hash_bytes).decode('utf-8')
    return wallet_address

def generateKeys(nvals, q):
    A = random.sample(range(q), nvals)
    B = []
    min_value = 0
    max_value = nvals ** 4
    secret_vector = [random.randint(min_value, max_value) for _ in range(nvals)]  # Secret key as an array
    secret_vector1 = [random.randint(min_value, max_value) for _ in range(nvals)]  # Secret key as an array
    secret_vector = [x % 256 for x in secret_vector]
    secret_vector1 = [x % 256 for x in secret_vector]
    s = sum(secret_vector) + sum(secret_vector1)
    e = [random.randint(1, 4) for _ in range(nvals)]
    for x in range(0,len(A)):
        B.append((A[x]*s+e[x])%q)
    return A, B, s, e, secret_vector, secret_vector1

def encrypt(message, A, B, q):
    nvals = len(A)
    sample = random.sample(range(nvals - 1), nvals // 4)
    u = sum(A[i] for i in sample) % q
    v = (sum(B[i] for i in sample) + math.floor(q // 2) * message) % q
    return u, v

def decrypt(u, v, s, q):
    res = (v - s * u) % q
    return 1 if res > q / 2 else 0