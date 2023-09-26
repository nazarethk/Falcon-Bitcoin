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

## Output
```
(base) nazarethkeshishian@Nazareths-MacBook-Pro LWE-bitcoin % python LWE.py 
Enter a string to encrypt: Hello World!
010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001

------Parameters and keys-------
Message to send:         Hello World!
Public Key (A):  [67, 10, 87, 13, 76, 38, 78, 89, 25, 52, 39, 65, 35, 45, 54, 21]
Public Key (B):  [59, 14, 87, 49, 62, 31, 84, 13, 83, 88, 43, 38, 95, 12, 16, 41]
Errors (e):              [1, 1, 3, 3, 2, 1, 2, 4, 2, 1, 2, 2, 1, 2, 4, 4]
Secret vector:           [225, 116, 220, 112, 234, 188, 156, 249, 149, 147, 115, 254, 66, 227, 10, 205, 225, 116, 220, 112, 234, 188, 156, 249, 149, 147, 115, 254, 66, 227, 10, 205]
Secret key:              5346
Prime number:            97
Decrypted bits are: [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
Decrypted message:  Hello World!
Public key: 00430a570d4c264e5919342741232d36153b0e57313e1f540d53582b265f0c1029 33.0 bytes
Private key: e174dc70eabc9cf9959373fe42e30acde174dc70eabc9cf9959373fe42e30acd 32.0 bytes
wallet_address: 1EVLsNHEz7cNAQBJY8ym9JFSNBFMA7WKF5 34 base58 characters, representing 25 bytes
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1]
non_zero_indices [1, 2, 4, 6, 9, 12, 13, 15]
step2: c_coefficients [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1]
step3: c_coefficients [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1]
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1]
non_zero_indices [1, 2, 4, 5, 7, 11, 12, 13, 15]
step2: c_coefficients [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1]
step3: c_coefficients [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1]
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
non_zero_indices [1, 3, 5, 6, 13]
step2: c_coefficients [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
step3: c_coefficients [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
non_zero_indices [2, 3, 7, 9, 10, 12, 13, 14, 15]
step2: c_coefficients [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
step3: c_coefficients [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
Signature: ([0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1], [74, 65, 26, 37, 1, 85, 56, 16, 86, 30, 78, 37, 85, 73, 65, 56], [83, 68, 63, 8, 25, 1, 24, 67, 89, 20, 78, 82, 65, 22, 78, 72], [16, 37, 4, 67, 60, 52, 81, 0, 69, 31, 3, 81, 34, 61, 27, 62])
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
non_zero_indices [2, 3, 7, 9, 10, 12, 13, 14, 15]
step2: c_coefficients [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
step3: c_coefficients [0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
Signature is valid.
```
