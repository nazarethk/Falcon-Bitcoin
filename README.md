# Lattice-Based Encryption for Bitcoin Core
🔒 This repository contains an implementation of a lattice-based encryption scheme for Bitcoin Core, employing Learning With Errors (LWE) techniques. The project is organized into the following files:

## LWE_LIB.py

### Description
This file contains multiple utility functions essential for the lattice-based encryption process. These functions include:

- `stringToBinary`: Transforms a string into binary format (characters).
- `binaryToString`: Transforms binary format (characters) back into a string.
- `generatePublicKey`: Generates a 33-byte hexadecimal public key from two public vectors, A and B.
- `generatePrivateKey`: Generates a 32-byte hexadecimal private key from two public vectors, S1 and S2.
- `ripemd160`: Used to hash the public key to obtain a 160-bit wallet address.
- `generateWalletAddress`: Adds the byte prefix to the output of ripemd160, computes the checksum, and converts it into a base58 Bitcoin wallet address.
- `generateKeys`: Generates variables A, B, s, e, secret_vector, and secret_vector1.
- `encrypt`: Encrypts a message using the two public vectors, A and B.
- `decrypt`: Decrypts the encrypted tuple (u, v) with the secret key s (which is the sum of the values of both vectors secret_vector and secret_vector1).

## signatures.py

### Description
This file is dedicated to generating and validating signatures. It implements the GLYPH digital signature scheme used in conjunction with the Ring Learning With Errors (RLWE) encryption algorithm. For more information, please refer to the [Wikipedia page on Ring Learning With Errors signatures](https://en.wikipedia.org/wiki/Ring_learning_with_errors_signature).

## LWE.py



### Description

"LWE.py" is the core implementation file of the Lattice-Based Encryption for Bitcoin Core project. It encapsulates the essential functionality required for encrypting, decrypting, generating keys, creating wallet addresses, and handling digital signatures within the lattice-based encryption scheme. Below, we provide a breakdown of the key components and their functions:

### Main Function

The `main` function serves as the entry point for the program. It takes an `input_string` as a parameter, which represents the plaintext message you want to encrypt. The main tasks of the `main` function include:

1. **Binary Conversion**: The input string is converted into a binary format using the `stringToBinary` function.

2. **Key Generation**: Public and private keys, as well as other parameters required for encryption and decryption, are generated using the `generateKeys` function. These keys include:
   - Public Keys (A and B)
   - Secret Key (s)
   - Error Vector (e)
   - Secret Vectors (secret_vector and secret_vector1)

3. **Displaying Parameters**: The main function displays the following key parameters:
   - The original message to send.
   - Public Keys (A and B).
   - Error Vector (e).
   - Secret Vector (secret_vector + secret_vector1).
   - Secret Key (s).
   - The prime number used (q).

### Encryption and Decryption

The `main` function proceeds to encrypt and then decrypt the binary message. The steps involved are as follows:

1. **Encryption**: Each binary digit in the input message is encrypted using the `encrypt` function. This results in a pair of values (u, v) that represent the ciphertext.

2. **Decryption**: The encrypted ciphertext (u, v) is decrypted using the `decrypt` function with the secret key (s) and the prime number (q). The decrypted bits are collected and combined to form the original binary message.

### Wallet Address Generation

The code also demonstrates the generation of a Bitcoin wallet address from the public key using the following steps:

1. **Public Key Generation**: The public key is generated from the public vectors (A and B) using the `generatePublicKey` function.

2. **Wallet Address Creation**: The `generateWalletAddress` function is employed to create a Bitcoin wallet address from the public key. This process involves adding a byte prefix, computing the checksum, and converting the result into a base58 Bitcoin wallet address format.

### Digital Signature

This code file also includes functionality for generating and verifying digital signatures based on the GLYPH digital signature scheme used with Ring Learning With Errors (RLWE) encryption. This includes:

- Signature Generation: The `generateSignature` function generates a digital signature for the binary message using the public key, prime number, and other parameters.

- Signature Verification: The `verifySignature` function checks the validity of a digital signature by comparing it to the original binary message and the public key.

