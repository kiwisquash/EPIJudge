from test_framework import generic_test


def count_bits(x):
    # TODO - you fill in here.

    # Brute force O(n), n = number of bits
    # count = 0
    # while x:
    #     count += x & 1
    #     x >>= 1
    # return count

    # Count the number of 1s by clearing out the lowest "1" each time. 
    # O(k), k = number of 1s
    # count = 0
    # while x:
    #     count += 1
    #     x &= (x-1)
    # return count

    # Assuming that all numbers are 64 bits, we can use caching.
    # Strategy: 
    #    - Precompute the counts for all 16 bit numbers. 
    #    - Algorithm divides the 64 bit number into 4 pieces
    #    - Calculate the number of 1s in each piece
    #    - Add
    
    cache_cap = 2**16
    cache = []
    for x in range(cache_cap):
        cache.append(count_small_bits(x))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
