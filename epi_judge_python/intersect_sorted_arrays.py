from test_framework import generic_test

import bisect

def index(a,x):
    i = bisect.bisect_left(a, x)
    if i !=len(a) and a[i] == x:
        return i
    return -1

def intersect_two_sorted_arrays(A, B):

    if len(A) > len(B):
        A, B = B, A

    output = []
    for a in A:
        if index(B,a)!=-1 and index(output,a)==-1:
            output.append(a)
    return output

    # i = 0 #smaller
    # j = 0 #larger

    # output = []
    # prev = -float("inf")
    # while i < len(A) and j < len(B):
    #     if A[i] == B[j] and A[i] != prev:
    #         output.append(A[i])
    #         prev = A[i]
    #     if A[i] > B[j]:
    #         A, B = B, A
    #         i, j = j, i
    #     i+=1

    # return output

    # arrs = [A, B]
    # inds = [0, 0]
    # current = 0 if arrs[0][0] < arrs[1][0] else 1
    # output = []
    # while inds[0] < len(arrs[0]) and inds[1] < len(arrs[1]):

    #     while arrs[current][inds[current]] < arrs[current^1][inds[current^1]]:
    #         inds[current] +=1
    #         if inds[current] == len(arrs[current]):
    #             break

    #     if inds[current] == len(arrs[current]):
    #         break

    #     if arrs[current][inds[current]] == arrs[current^1][inds[current^1]]:

    #         add_val = arrs[current][inds[current]]
    #         output.append(add_val)

    #         while arrs[current][inds[current]] == add_val and arrs[current^1][inds[current^1]] == add_val:
    #             inds[current]+=1
    #             if inds[current] == len(arrs[current]):
    #                 break
    #             inds[current^1]+=1
    #             if inds[current^1] == len(arrs[current^1]):
    #                 break
    #     if inds[current] == len(arrs[current]):
    #         break

    #     if inds[current^1] == len(arrs[current^1]):
    #         break

    #     current = current if arrs[current][inds[current]] < arrs[current^1][inds[current^1]] else current^1

    # return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
