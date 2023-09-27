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
- `printParameters`: prints the parameters and keys used in the encryption / decryption process
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

3. **Displaying Parameters**: `printParameters` function displays the following key parameters:
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
Public Key (A):  [91, 1, 42, 66, 43, 62, 46, 72, 81, 80, 8, 48, 2, 94, 74, 51]
Public Key (B):  [49, 61, 69, 77, 28, 46, 4, 33, 62, 5, 71, 21, 20, 27, 50, 1]
Errors (e):              [3, 4, 3, 1, 2, 4, 1, 3, 4, 4, 3, 1, 3, 4, 3, 4]
Secret vector:           [70, 177, 26, 232, 86, 167, 151, 28, 177, 149, 176, 163, 162, 214, 108, 125, 70, 177, 26, 232, 86, 167, 151, 28, 177, 149, 176, 163, 162, 214, 108, 125]
Secret key:              4422
Prime number:            97
Encrypted tuples are: [(94, 34), (34, 54), (87, 24), (79, 49), (43, 85), (35, 68), (45, 55), (38, 43), (75, 18), (20, 33), (36, 75), (34, 12), (51, 7), (38, 90), (86, 63), (68, 54), (19, 28), (93, 26), (57, 5), (23, 62), (64, 24), (57, 11), (82, 25), (57, 54), (11, 59), (40, 11), (66, 39), (64, 73), (85, 51), (15, 44), (2, 27), (4, 47), (28, 58), (79, 5), (5, 55), (38, 44), (83, 34), (52, 16), (43, 83), (51, 57), (88, 81), (1, 67), (35, 18), (66, 87), (62, 51), (1, 69), (75, 19), (47, 74), (16, 52), (42, 26), (93, 74), (15, 37), (49, 87), (40, 12), (75, 68), (30, 26), (46, 14), (51, 58), (14, 83), (11, 58), (78, 43), (65, 77), (38, 94), (39, 51), (91, 60), (51, 55), (42, 31), (26, 86), (52, 65), (75, 17), (34, 59), (86, 64), (48, 31), (20, 35), (56, 48), (53, 28), (15, 43), (75, 65), (79, 51), (23, 64), (94, 33), (34, 54), (5, 55), (4, 49), (28, 55), (6, 11), (25, 80), (75, 20), (10, 96), (26, 38), (14, 82), (67, 46), (44, 1), (53, 23), (80, 15), (24, 72)]
Decrypted bits are: [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
Decrypted message:  Hello World!
Public key: 005b012a422b3e2e4851500830025e4a33313d454d1c2e04213e054715141b3201 33.0 bytes
Private key: 46b11ae856a7971cb195b0a3a2d66c7d46b11ae856a7971cb195b0a3a2d66c7d 32.0 bytes
wallet_address: 15PCKhMmY6KmJARjY5buChhxTXZNc8BdwA 34 base58 characters, representing 25 bytes
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1]
non_zero_indices [3, 4, 5, 6, 9, 10, 11, 14, 15]
step2: c_coefficients [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1]
step3: c_coefficients [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1]
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1]
non_zero_indices [2, 5, 6, 11, 12, 14, 15]
step2: c_coefficients [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1]
step3: c_coefficients [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1]
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
non_zero_indices [1, 3, 4, 5, 12]
step2: c_coefficients [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
step3: c_coefficients [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
non_zero_indices [1, 2, 4, 5, 6, 10, 12, 15]
step2: c_coefficients [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
step3: c_coefficients [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0]
non_zero_indices [2, 4, 5, 6, 7, 9, 10, 13, 14]
step2: c_coefficients [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0]
step3: c_coefficients [0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0]
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
non_zero_indices [2, 4, 5, 6, 14]
step2: c_coefficients [0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
step3: c_coefficients [0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0]
non_zero_indices [1, 6, 10, 12, 13]
step2: c_coefficients [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0]
step3: c_coefficients [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0]
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1]
non_zero_indices [6, 7, 9, 12, 14, 15]
step2: c_coefficients [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1]
step3: c_coefficients [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1]
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0]
non_zero_indices [1, 3, 4, 5, 6, 7, 12, 13]
step2: c_coefficients [0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0]
step3: c_coefficients [0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0]
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]
non_zero_indices [3, 5, 6, 9, 10, 11, 12, 13, 14, 15]
step2: c_coefficients [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]
step3: c_coefficients [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]
Signature: ([0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], [34, 50, 88, 61, 1, 50, 85, 81, 37, 33, 61, 22, 33, 43, 13, 25], [21, 90, 25, 35, 36, 56, 80, 70, 42, 77, 46, 39, 84, 5, 55, 68], [12, 23, 72, 32, 31, 96, 3, 90, 29, 64, 66, 31, 11, 9, 4, 5])
step0: c_coefficients [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
step1: c_coefficients [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]
non_zero_indices [3, 5, 6, 9, 10, 11, 12, 13, 14, 15]
step2: c_coefficients [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]
step3: c_coefficients [0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]
Signature is valid.
```
