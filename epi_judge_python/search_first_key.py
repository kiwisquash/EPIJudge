from test_framework import generic_test


def search_first_of_k(A, k):
    L = 0
    R = len(A) - 1
    # if R == -1: return -1 # this is only needed if I plan to reference M outside of the while loop
    while L <= R:
        M = L + (R - L) // 2
        if A[M] < k:
            L = M + 1
        elif A[M] > k:
            R = M - 1
        else: # A[M] is k here
            if M == 0 or A[M-1]!=k: return M 
            R = M - 1
    return -1
    # This gives O(n) worst case. Is that what we want to settle for?
            # break
    # while M>=0 and A[M] == k:
        # M-=1
    # return M + 1 if L <= R else -1 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
