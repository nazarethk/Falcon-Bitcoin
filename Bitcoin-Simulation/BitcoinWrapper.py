from falcon import decompress, sub_zq, mul_zq, q, HEAD_LEN, SALT_LEN
from Crypto.Hash import SHAKE256
from cryptos import sha256, ripemd160

"""
 FalconParam(256, 64)
    256: {
        "n": 256,
        "sigma": 163.04153322607107,
        "sigmin": 1.2570545284063217,
        "sig_bound": 16468416,
        "sig_bytelen": 356,
    },
    # FalconParam(512, 128)
    512: {
        "n": 512,
        "sigma": 165.7366171829776,
        "sigmin": 1.2778336969128337,
        "sig_bound": 34034726,
        "sig_bytelen": 666,
    },
    # FalconParam(1024, 256)
    1024: {
        "n": 1024,
        "sigma": 168.38857144654395,
        "sigmin": 1.298280334344292,
        "sig_bound": 70265242,
        "sig_bytelen": 1280,
    },"""

n = 256
sig_bytelen = 356 # for falcon 256
sig_bound = 16468416 # for falcon 256


def hash_to_point(message, salt):
        """
        Hash a message to a point in Z[x] mod(Phi, q).
        Inspired by the Parse function from NewHope.
        """
        if q > (1 << 16):
            raise ValueError("The modulus is too large")

        k = (1 << 16) // q
        # Create a SHAKE object and hash the salt and message.
        shake = SHAKE256.new()
        shake.update(salt)
        shake.update(message)
        # Output pseudorandom bytes and map them to coefficients.
        hashed = [0 for i in range(n)]
        i = 0
        j = 0
        while i < n:
            # Takes 2 bytes, transform them in a 16 bits integer
            twobytes = shake.read(2)
            elt = (twobytes[0] << 8) + twobytes[1]  # This breaks in Python 2.x
            # Implicit rejection sampling
            if elt < k * q:
                hashed[i] = elt % q
                i += 1
            j += 1
        return hashed


def verify(scriptSig, message, scriptPubKey):
        len_signature = sig_bytelen * 2

        # Extract the signature based on the length
        signature = scriptSig[len(str(len_signature)) : len(str(len_signature)) + len_signature]

        len_pubkey = len(str(1024))

        # Extract the pubkey based on the length
        pubkey = scriptSig[len(str(len_signature)) + len_signature + len_pubkey :]
        hash160 = ripemd160(sha256(pubkey))

        if scriptPubKey != ("76a9" + str(len(hash160)) + hash160 + "88ac"):
            print("OP_EQUALVERIFY failed")
            return False
        
        h =  [int(pubkey[i:i+4], 16) for i in range(0, len(pubkey), 4)]
        print(h)
        """
        Verify a signature.
        """
        # Unpack the salt and the short polynomial s1
        signature = bytes.fromhex(signature)
        salt = signature[HEAD_LEN:HEAD_LEN + SALT_LEN]
        enc_s = signature[HEAD_LEN + SALT_LEN:]
        s1 = decompress(enc_s, sig_bytelen - HEAD_LEN - SALT_LEN, n)

        # Check that the encoding is valid
        if (s1 is False):
            print("Invalid encoding")
            return False

        # Compute s0 and normalize its coefficients in (-q/2, q/2]
        hashed = hash_to_point(message, salt)
        s0 = sub_zq(hashed, mul_zq(s1, h))
        s0 = [(coef + (q >> 1)) % q - (q >> 1) for coef in s0]

        # Check that the (s0, s1) is short
        norm_sign = sum(coef ** 2 for coef in s0)
        norm_sign += sum(coef ** 2 for coef in s1)
        if norm_sign > sig_bound:
            print("Squared norm of signature is too large:", norm_sign)
            print("OP_CHECKSIG failed")
            return False
        
        # If all checks are passed, accept
        return True
