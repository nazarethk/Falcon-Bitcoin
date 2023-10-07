#ifndef UTILS_H
#define UTILS_H

#include <stdint.h>
#include <stddef.h>

void mergeUint8Arrays(const uint8_t *array1, size_t size1, const uint8_t *array2, size_t size2, uint8_t *result, size_t *result_size);

#endif
