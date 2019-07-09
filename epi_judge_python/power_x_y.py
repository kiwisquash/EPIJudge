from test_framework import generic_test


def power(x, y):
    # TODO - you fill in here.
    if y < 0:
        y = -y
        x = 1/x
    # if y== 0: return 1
    # if y % 2 == 0: return pow(x*x, y//2)
    # if y % 2 == 1: return x*pow(x, y-1)
    output = 1
    while y:
        if y % 2 == 0:
            x *=x
            y //=2
        else:
            output *=x
            y-=1
    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
