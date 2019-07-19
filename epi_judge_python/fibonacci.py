from test_framework import generic_test



def fibonacci(n):
    prev = 1
    next = 0
    for _ in range(n):
        prev, next = next, prev + next
    return next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("fibonacci.py", 'fibonacci.tsv',
                                       fibonacci))
