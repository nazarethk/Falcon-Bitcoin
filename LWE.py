"""
# This file contains the main code.
"""
from LWE_LIB import generateWalletAddress, stringToBinary, binaryToString, generatePublicKey, generatePrivateKey, generateKeys, encrypt, decrypt
from signatures import generateSignature, verifySignature

def main(input_string):
    binary_string = stringToBinary(input_string)
    print(binary_string)
    nvals = 16
    q = 97
    A, B, s, e, secret_vector, secret_vector1= generateKeys(nvals, q)
    print("\n------Parameters and keys-------")
    print("Message to send:\t", input_string)
    print("Public Key (A):\t", A)
    print("Public Key (B):\t", B)
    print("Errors (e):\t\t", e)
    print("Secret vector:\t\t",  secret_vector+ secret_vector1 )
    print("Secret key:\t\t", s)
    print("Prime number:\t\t", q)
    decrypted_bits = []
    for message in binary_string:
        message = int(message)
        u, v = encrypt(message, A,B, q)
        decrypted_message = decrypt(u, v, s, q)
        decrypted_bits.append(decrypted_message)

    print("Decrypted bits are:", decrypted_bits)
    print("Decrypted message: ", binaryToString( ''.join(map(str, decrypted_bits))))
    public_key = generatePublicKey(A,B)
    print("Public key:", public_key, len(public_key)/2, "bytes")
    private_key = generatePrivateKey(secret_vector, secret_vector1)
    print("Private key:", private_key, len(private_key)/2, "bytes")
    wallet_address = generateWalletAddress(public_key)
    print("wallet_address:", wallet_address, len(wallet_address), "base58 characters, representing 25 bytes")
    signature = generateSignature(binary_string, A, q, nvals)
    print("Signature:", signature)
    is_valid = verifySignature(signature, A, binary_string, nvals, q)
    if is_valid:
        print("Signature is valid.")
    else:
        print("Signature is invalid.")


if __name__ == "__main__":
    input_string = input("Enter a string to encrypt: ")
    main(input_string)
