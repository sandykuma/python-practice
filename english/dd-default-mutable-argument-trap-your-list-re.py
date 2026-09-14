"""Mutable default trap 😱
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

def add_score(name, scores={}):
    scores[name] = scores.get(name, 0) + 1
    return scores
# TODO: Fix the mutable default dict so each call gets a new dict


# ---- SOLUTION (peek only after trying!) ----
# def add_item(item, lst=None):
#     lst = [] if lst is None else lst; lst.append(item); return lst
# 
# print(add_item(1), add_item(2))
# # [1] [2]
