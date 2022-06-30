def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    soreted_scores = sorted(scores)
    mid_list = soreted_scores[::-1]
    final_list = mid_list[0:3]
    return final_list
