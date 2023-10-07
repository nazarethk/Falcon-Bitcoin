#include "utils.h"
#include <string.h>

void mergeUint8Arrays(const uint8_t *array1, size_t size1, const uint8_t *array2, size_t size2, uint8_t *result, size_t *result_size)
{
    // Calculate the size of the concatenated array
    *result_size = size1 + size2;

    // Copy the contents of array1 into the result array
    memcpy(result, array1, size1);

    // Copy the contents of array2 into the result array starting from the end of array1
    memcpy(result + size1, array2, size2);
}
