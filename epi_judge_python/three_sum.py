from test_framework import generic_test


def has_three_sum(A, t):
    A.sort()
    for a in A:
        tar = t - a
        i, j = 0, len(A) - 1
        while i <= j:
            if tar < A[i] + A[j]:
                j-=1
            elif tar > A[i] + A[j]:
                i+=1
            else:
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
