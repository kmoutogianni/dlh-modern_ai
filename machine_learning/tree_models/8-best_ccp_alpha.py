#!/usr/bin/env python3
"""Selects the best ccp_alpha for pruning."""


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    """Selects the best pruning parameter and classifier."""

    # 1. Find the highest test accuracy
    best_test_score = max(test_scores)

    # 2. Keep the indices of models with the highest test accuracy
    candidates = [
        i for i, score in enumerate(test_scores)
        if score == best_test_score
    ]

    # 3. Find the smallest difference between training and test accuracy
    best_diff = min(
        abs(train_scores[i] - test_scores[i])
        for i in candidates
    )

    # 4. Keep only models with the smallest difference
    candidates = [
        i for i in candidates
        if abs(train_scores[i] - test_scores[i]) == best_diff
    ]

    # 5. If there is still a tie, choose the largest ccp_alpha
    best_index = max(candidates, key=lambda i: ccp_alphas[i])

    best_alpha = ccp_alphas[best_index]
    best_clf = clfs[best_index]

    return best_alpha, best_clf
