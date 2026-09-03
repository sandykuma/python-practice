"""defaultdict हर key याद रखता है 😱
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

from collections import defaultdict
counts = defaultdict(int)
counts['apple'] += 1
# TODO: access 'banana' and print its count


# ---- SOLUTION (peek only after trying!) ----
# from collections import defaultdict
# d = defaultdict(list)
# _ = d['new']
# print('new' in d)  # True
