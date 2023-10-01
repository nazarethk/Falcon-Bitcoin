"""
# This file is used to generate and validate signatures. It is the GLYPH digital signature scheme used with Ring learning with errors encryption algo.
# Reference: https://en.m.wikipedia.org/wiki/Ring_learning_with_errors_signature
"""
import random
B = 16383 # Security parameter
k = 16   # Number of non-zero coefficients in c(x)

def encodePolynomial(coefficients):
    # Encode the coefficients of a polynomial as a bit string
    # Each coefficient is represented as a binary string with a fixed number of bits
    bits_per_coefficient = 8  # 8 bits per coefficient
    encoded_bits = ''.join(format(c, f'0{bits_per_coefficient}b') for c in coefficients)
    return encoded_bits

def polyHash(bits, nvals, q):
    # Hash the concatenated bit string and return c(x) as a polynomial
    c_coefficients = [0] * nvals
    # print("step0: c_coefficients", c_coefficients)

    for i, bit in enumerate(bits):
        if bit == '1':
            c_coefficients[i % nvals] ^= 1
    # print("step1: c_coefficients", c_coefficients)

    non_zero_indices = [i for i, coeff in enumerate(c_coefficients) if coeff != 0]
    # print("non_zero_indices", non_zero_indices)

    if len(non_zero_indices) > k:
        for i in range(len(non_zero_indices) - k):
            c_coefficients[non_zero_indices[i]] = 0
    # print("step2: c_coefficients", c_coefficients)

    c_coefficients = [coeff % q for coeff in c_coefficients]
    # print("step3: c_coefficients", c_coefficients)

    return c_coefficients

def generateSignature(message, a_coefficients, q, nvals):
    while True:
        y1_coefficients = [random.randint(-B, B) for _ in range(nvals)]
        y2_coefficients = [random.randint(-B, B) for _ in range(nvals)]

        w_coefficients = [(a * y1 + y2) % q for a, y1, y2 in zip(a_coefficients, y1_coefficients, y2_coefficients)]

        omega = encodePolynomial(w_coefficients)

        concatenated_message = omega + message
        c_coefficients = polyHash(concatenated_message, nvals, q)

        s_coefficients = [random.randint(-B, B) for _ in range(nvals)]
        e_coefficients = [random.randint(-B, B) for _ in range(nvals)]

        z1_coefficients = [(s * c + y1) % q for s, c, y1 in zip(s_coefficients, c_coefficients, y1_coefficients)]
        z2_coefficients = [(e * c + y2) % q for e, c, y2 in zip(e_coefficients, c_coefficients, y2_coefficients)]

        infinity_norm_z1 = max([abs(coeff) for coeff in z1_coefficients])
        infinity_norm_z2 = max([abs(coeff) for coeff in z2_coefficients])
        beta = B - k
        print(infinity_norm_z1, beta, infinity_norm_z2)
        if infinity_norm_z1 <= beta and infinity_norm_z2 <= beta:
            # Compute t(x) = a(x)·s(x) + e(x) and return it as part of the public key
            t_coefficients = [(a * s + e) % q for a, s, e in zip(a_coefficients, s_coefficients, e_coefficients)]
            return c_coefficients, z1_coefficients, z2_coefficients, t_coefficients

def verifySignature(signature, public_key, message, nvals, q):
    c_coefficients, z1_coefficients, z2_coefficients, t_coefficients = signature

    beta = B - k
    infinity_norm_z1 = max([abs(coeff) for coeff in z1_coefficients])
    infinity_norm_z2 = max([abs(coeff) for coeff in z2_coefficients])

    if infinity_norm_z1 > beta or infinity_norm_z2 > beta:
        return False

    w_prime_coefficients = [(a * z1 + z2 - t * c) % q for a, z1, z2, t, c in zip(public_key, z1_coefficients, z2_coefficients, t_coefficients, c_coefficients)]
    omega_prime = encodePolynomial(w_prime_coefficients)

    concatenated_message = omega_prime + message
    c_prime_coefficients = polyHash(concatenated_message, nvals, q)

    return c_prime_coefficients == c_coefficients
