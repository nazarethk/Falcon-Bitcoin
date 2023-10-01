"""
# This file contains the main code.
"""
from LWE_LIB import generateWalletAddress, printParameters, stringToBinary, binaryToString, generatePublicKey, generatePrivateKey, generateKeys, encrypt, decrypt
from signatures import generateSignature, verifySignature

def main(input_string, nvals, q):
    binary_string = stringToBinary(input_string)
    print(binary_string)
    A, B, s, e, secret_vector, secret_vector1 = generateKeys(nvals, q)
    printParameters(input_string, A, B, e, secret_vector, secret_vector1, s, q)
    decrypted_bits = []
    encrypted_tuples = []
    for message in binary_string:
        message = int(message)
        u, v = encrypt(message, A,B, q)
        decrypted_message = decrypt(u, v, s, q)
        decrypted_bits.append(decrypted_message)
        encrypted_tuples.append((u,v))

    print("Encrypted tuples are:", encrypted_tuples)
    print("Decrypted bits are:", decrypted_bits)
    print("Decrypted message: ", binaryToString( ''.join(map(str, decrypted_bits))))
    public_key = generatePublicKey(A,B)
    print("Public key:", public_key, len(public_key)/2, "bytes")
    private_key = generatePrivateKey(secret_vector, secret_vector1)
    print("Private key:", private_key, len(private_key)/2, "bytes")
    wallet_address = generateWalletAddress(public_key)
    print("wallet_address:", wallet_address, len(wallet_address), "base58 characters, representing 25 bytes")
    # signature = generateSignature(binary_string, A, q, nvals)
    # print("Signature:", signature)
    # is_valid = verifySignature(signature, A, binary_string, nvals, q)
    # if is_valid:
    #     print("Signature is valid.")
    # else:
    #     print("Signature is invalid.")

if __name__ == "__main__":
    nvals = 1024
    q = 59393
    input_string = input("Enter a string to encrypt: ")
    main(input_string, nvals, q)
