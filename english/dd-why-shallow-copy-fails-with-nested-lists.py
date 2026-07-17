"""Shallow Copy 🚫 Nested Lists
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

data = [{'a': 1}, {'b': 2}]
copy_data = data.copy()  # TODO: use deepcopy to avoid mutating originals
copy_data[0]['a'] = 99
print(data)  # Should remain unchanged


# ---- SOLUTION (peek only after trying!) ----
# import copy
# orig = [[1, 2], [3, 4]]
# deep = copy.deepcopy(orig)
# deep[0][0] = 99
# print(orig)  # [[1, 2], [3, 4]]
