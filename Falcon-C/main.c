#include <time.h>
#include <string.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include "api.h"
#include "katrng.h"
#include "sha256.h"
#include "ripemd160/ripemd160.h"
#include "base58/libbase58.h"
#include "utils.h"
#define MLEN 59

int main(void)
{
    size_t i, j;
    int ret;
    size_t mlen, smlen;
    uint8_t b;
    uint8_t m[MLEN + CRYPTO_BYTES];
    uint8_t m2[MLEN + CRYPTO_BYTES];
    uint8_t sm[MLEN + CRYPTO_BYTES];
    uint8_t pk[CRYPTO_PUBLICKEYBYTES];
    uint8_t sk[CRYPTO_SECRETKEYBYTES];

    uint8_t entropy_input[MLEN + CRYPTO_BYTES];
    int count = 0;

    srand((unsigned int)time(NULL));

    while (count < MLEN + CRYPTO_BYTES)
    {
        uint8_t c = (uint8_t)(rand() % 256); // Generate random byte (0-255)
        entropy_input[count] = c;
        count++;
    }

    printf("Entropy collected successfully.\n");
    uint8_t personalization_string[32];
    int security_strength = 256;

    randombytes_init(entropy_input, personalization_string, security_strength);

    // Generate random data for m
    randombytes(m, MLEN);

    crypto_sign_keypair(pk, sk);
    crypto_sign(sm, &smlen, m, MLEN, sk);
    ret = crypto_sign_open(m2, &mlen, sm, smlen, pk);

    if (ret)
    {
        fprintf(stderr, "Verification failed\n");
        return -1;
    }
    if (mlen != MLEN)
    {
        fprintf(stderr, "Message lengths wrong\n");
        return -1;
    }
    for (j = 0; j < MLEN; ++j)
    {
        if (m2[j] != m[j])
        {
            fprintf(stderr, "Messages don't match\n");
            return -1;
        }
    }

    randombytes((uint8_t *)&j, sizeof(j));
    do
    {
        randombytes(&b, 1);
    } while (!b);
    sm[j % (MLEN + CRYPTO_BYTES)] += b;
    ret = crypto_sign_open(m2, &mlen, sm, smlen, pk);
    if (!ret)
    {
        fprintf(stderr, "Trivial forgeries possible\n");
        return -1;
    }

    printf("NAME: %s\n", CRYPTO_ALGNAME);
    printf("CRYPTO_PUBLICKEYBYTES = %d\n", CRYPTO_PUBLICKEYBYTES);
    printf("CRYPTO_SECRETKEYBYTES = %d\n", CRYPTO_SECRETKEYBYTES);
    printf("CRYPTO_BYTES = %d\n", CRYPTO_BYTES);
    printf("Signature Length = %ld\n", smlen);

    printf("\nAlice Public key: %s\n", showhex(pk, CRYPTO_PUBLICKEYBYTES));
    printf("\nAlice Secret key: %s\n", showhex(sk, CRYPTO_SECRETKEYBYTES));

    uint8_t public_key_hash[32];
    generateSHA256(pk, strlen((char *)showhex(pk, CRYPTO_PUBLICKEYBYTES)), public_key_hash, "\nAlice public key hashed");

    uint8_t ripmed_160_hash[20];
    generateRIPEMD160(pk, strlen((char *)showhex(pk, CRYPTO_PUBLICKEYBYTES)), ripmed_160_hash, "\nripmed_160_hash");
    uint8_t hash_with_version[21];

    // Add the version byte (0x00) at the beginning
    hash_with_version[0] = 0x00;
    memcpy(hash_with_version + 1, ripmed_160_hash, sizeof(ripmed_160_hash));

    uint8_t checksum[4];
    generateChecksum(hash_with_version, sizeof(hash_with_version), checksum);

    size_t size1 = sizeof(hash_with_version) / sizeof(hash_with_version[0]);
    size_t size2 = sizeof(checksum) / sizeof(checksum[0]);

    size_t result_size = size1 + size2;

    uint8_t result[result_size];
    mergeUint8Arrays(hash_with_version, size1, checksum, size2, result, &result_size);

    char base58_encoded[50];
    size_t base58_encoded_size = sizeof(base58_encoded);
    b58enc(base58_encoded, &base58_encoded_size, result, result_size);

    uint8_t private_key_hash[32];
    generateSHA256(sk, strlen((char *)showhex(sk, CRYPTO_SECRETKEYBYTES)), private_key_hash, "\nAlice private key hashed");

    printf("\nMessage: %s\n", showhex(m, MLEN));
    printf("\nSignature : %s\n", showhex(sm, smlen));
    printf("Verified!\n");
    free(showhex(pk, CRYPTO_PUBLICKEYBYTES));
    free(showhex(sk, CRYPTO_SECRETKEYBYTES));
    return 0;
}
