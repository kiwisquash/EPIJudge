from test_framework import generic_test
from test_framework.test_failure import TestFailure


def d_to_c(d):
    return chr(d + ord("0"))

def c_to_d(c):
    return ord(c) - ord("0")

def int_to_string(x):
    # TODO - you fill in here.
    if x == 0: return "0"
    temp = abs(x)
    c_list = []
    while temp:
        d = temp % 10
        temp //= 10
        c_list.append(d_to_c(d))
    if x<0:
        c_list.append("-")
    return ''.join(reversed(c_list)) 

def string_to_int(s):
    # TODO - you fill in here.
    is_neg = False
    num = 0
    for i, c in enumerate(s):
        if i == 0 and c == "-":
            is_neg = True
        else:
            num = 10*num + c_to_d(c)
    return num*-1 if is_neg else num

def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
