def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    outcome = sorted(scores, reverse=True)
    return outcome[:3]
