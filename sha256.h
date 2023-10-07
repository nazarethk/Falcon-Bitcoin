#ifndef SHA256_H
#define SHA256_H

#include <stdint.h>

#define SHA256_BLOCK_SIZE 64

typedef struct
{
    uint8_t data[64];
    uint32_t datalen;
    uint64_t bitlen;
    uint32_t state[8];
} SHA256_CTX;

void sha256_init(SHA256_CTX *ctx);
void sha256_update(SHA256_CTX *ctx, const uint8_t data[], size_t len);
void sha256_final(SHA256_CTX *ctx, uint8_t hash[32]);
void generateSHA256(uint8_t hash[32], const uint8_t data[], size_t len, const char *description);

#endif /* SHA256_H */
