import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    # TODO - you fill in here.
    n = len(A)
    pivot = A[pivot_index]
    equal = small = 0
    large = n - 1
   
    while (equal<=large):
        if A[equal] < pivot:
            A[equal], A[small] = A[small], A[equal]
            small +=1
            equal +=1 # Because equal is attached to small, it gets pushed along
        elif A[equal] > pivot:
            A[equal], A[large] = A[large], A[equal]
            large -=1
        else:
            equal +=1

    # n = len(A)
    # pivot = A[pivot_index]
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if A[j] < pivot:
    #             A[i], A[j] = A[j], A[i]

    # for i in reversed(range(n)):
    #     for j in reversed(range(i)):
    #         if A[j] > pivot:
    #             A[i], A[j] = A[j], A[i]

    # n = len(A)
    # pivot = A[pivot_index]
    # small = 0
    # for i in range(n):
    #     if A[i]< pivot:
    #         A[small], A[i] = A[i], A[small]
    #         small+=1
    # large = n - 1
    # for j in reversed(range(n)):
    #     if A[j] > pivot:
    #         A[large], A[j] = A[j], A[large]
    #         large-=1
    # print(A)
    # next_less = 0
    # next_more = next_eq = len(A) - 1
    # pivot = A[pivot_index]
    # while (next_less < next_more):
    #     if A[next_less] < pivot:
    #         next_less +=1
    #     elif A[next_less] > pivot:
    #         A[next_less], A[next_more] = A[next_more], A[next_less]
    #         next_more -=1
    #     else:
    #         A[next_less], A[next_eq] = A[next_eq], A[next_less]
    #         if next_more == next_eq:
    #             next_more -=1
    #         next_eq -=1
    # start = next_more if A[next_more] > A[-1] else next_more + 1
    # runner = 0
    # print("Pre-array:", A)
    # for i in range(start, next_eq+1):
    #     A[i], A[-1-runner] = A[-1-runner], A[i]
    #     runner +=1
    # print("Final array:", A)
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
