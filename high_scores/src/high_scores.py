def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


# def personal_top_three(scores):
#     soreted_scores = sorted(scores)
#     mid_list = soreted_scores[::-1]
#     final_list = mid_list[0:3]
#     return final_list


def personal_top_three(scores):
    final_list = []
    double_score = []
    sorted_scores = sorted(scores)
    reversed_scores = sorted_scores[::-1]
    top_4_list = reversed_scores[0:4]
    index = 0
    for score in reversed_scores:
        final_list.append(score)
        if reversed_scores[index] == reversed_scores[index - 1]:
            double_score.append(score)
            double_score.append(score)

            final_list.remove(reversed_scores[index - 1])
            final_list.remove(reversed_scores[index])

            final_list.append(double_score)

        index += 1
        # return final_list

    return final_list[0:3]


def ordered_list(scores):
    sorted_list = sorted(scores)
    final_list = sorted_list[::-1]
    return final_list
