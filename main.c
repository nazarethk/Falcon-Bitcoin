

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#include "api.h"
#include "katrng.h"

#define MLEN 59

char *showhex(uint8_t a[], int size);

char *showhex(uint8_t a[], int size)
{

    char *s = malloc(size * 2 + 1);

    for (int i = 0; i < size; i++)
        sprintf(s + i * 2, "%02x", a[i]);

    return (s);
}

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
    printf("Alice Secret key: %s\n", showhex(sk, CRYPTO_SECRETKEYBYTES));

    printf("\nMessage: %s\n", showhex(m, MLEN));
    printf("Signature : %s\n", showhex(sm, smlen));
    printf("Verified!\n");
    return 0;
}