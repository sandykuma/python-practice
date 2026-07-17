"""Deepcopy Fix 🚫
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

data = [{'a': 1}, {'b': 2}]
copy_data = data.copy()  # TODO: replace with deepcopy to avoid inner dict sharing
copy_data[0]['a'] = 99
print(data)  # Should stay unchanged


# ---- SOLUTION (peek only after trying!) ----
# import copy
# original = [[1, 2], [3, 4]]
# deep = copy.deepcopy(original)
# deep[0][0] = 88
# print(original)  # [[1, 2], [3, 4]]
