from falcon import decompress, sub_zq, mul_zq, q, HEAD_LEN, SALT_LEN
from Crypto.Hash import SHAKE256
from cryptos import sha256, ripemd160


falconParams = {
     64:{
        "n": 64,
        "sigma": 157.51308555044122,
        "sigmin": 1.2144300507766141,
        "sig_bound": 3842630,
        "sig_bytelen": 122,
    },128:{
        "n": 128,
        "sigma": 160.30114421975344,
        "sigmin": 1.235926056771981,
        "sig_bound": 7959734,
        "sig_bytelen": 200,
    }, 256:{
        "n": 256,
        "sigma": 163.04153322607107,
        "sigmin": 1.2570545284063217,
        "sig_bound": 16468416,
        "sig_bytelen": 356,
    }, 512:{
        "n": 512,
        "sigma": 165.7366171829776,
        "sigmin": 1.2778336969128337,
        "sig_bound": 34034726,
        "sig_bytelen": 666,
    }, 1024:{
        "n": 1024,
        "sigma": 168.38857144654395,
        "sigmin": 1.298280334344292,
        "sig_bound": 70265242,
        "sig_bytelen": 1280,
    }
}


def hash_to_point(message, salt, n):
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

def verify(scriptSig, message, scriptPubKey, n):
        sig_bytelen = falconParams[n]["sig_bytelen"] 
        sig_bound = falconParams[n]["sig_bound"]
        sig_len = n * 4 
        len_signature = sig_bytelen * 2
        print("len_signature", len_signature)
        # Extract the signature based on the length
        signature = scriptSig[len(str(len_signature)) : len(str(len_signature)) + len_signature]

        len_pubkey = len(str(sig_len))

        # Extract the pubkey based on the length
        pubkey = scriptSig[len(str(len_signature)) + len_signature + len_pubkey :]
        print("len_pubkey", len(pubkey))
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
        hashed = hash_to_point(message, salt, n)
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
