from test_framework import generic_test

from collections import Counter

def can_form_palindrome(s):
    # A palindrome of even length has even number of letters per char
    # A palindrome of odd length has exactly one char that is odd number, all others even
    char_nums = Counter(s)
    num_odds = 0
    for char in char_nums:
        num_odds += char_nums[char] % 2 # Counts the number of odds
    return num_odds <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
