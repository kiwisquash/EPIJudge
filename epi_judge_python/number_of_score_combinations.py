from test_framework import generic_test
from copy import copy


sub_memo = {
    1: 0,
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 2,
    7: 1,
}

memo = sub_memo.copy()

memo[7] +=1

def num_combinations_for_final_score(n, individual_play_scores):
    if n not in memo:
        if n - 3 not in sub_memo:
            sub_memo[n-3] = sub_memo[n-6] + 1^((n-5)%2)
        memo[n] = memo[n-7] + sub_memo[n-3] + 1^((n-2)%2)
    return memo[n] 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
