from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    table = [[0] * (final_score + 1) for _ in individual_play_scores]
    for i in range(len(individual_play_scores)):
        table[i][0] = 1
    for i in range(1, final_score + 1):
        for j in range(len(individual_play_scores)):
            table[j][i] = (table[j][i - individual_play_scores[j]] if (i - individual_play_scores[j]) >= 0 else 0) + (table[j - 1][i] if j >= 1 else 0)
    # TODO - you fill in here.
    return table[len(individual_play_scores) - 1][final_score]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
