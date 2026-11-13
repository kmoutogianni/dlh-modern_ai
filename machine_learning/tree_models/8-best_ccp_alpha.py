#!/usr/bin/env python3
"""module 8"""


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    """Selects the best pruning value for a set of trained decision trees"""

    best_test_score = max(test_scores)

    candidates = [
        i for i, score in enumerate(test_scores)
        if score == best_test_score
    ]

    best_diff = min(
        abs(train_scores[i] - test_scores[i])
        for i in candidates
    )

    candidates = [
        i for i in candidates
        if abs(train_scores[i] - test_scores[i]) == best_diff
    ]

    best_index = max(candidates, key=lambda i: ccp_alphas[i])

    best_alpha = ccp_alphas[best_index]
    best_clf = clfs[best_index]

    return best_alpha, best_clf
