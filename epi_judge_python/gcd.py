from test_framework import generic_test


def gcd(x, y):
    if x==0 or y==0:
        return x if y == 0 else y
    if x > y:
        return gcd(x % y, y)
    return gcd(x, y % x)


if __name__ == '__main__':
    exit(generic_test.generic_test_main("gcd.py", 'gcd.tsv', gcd))
