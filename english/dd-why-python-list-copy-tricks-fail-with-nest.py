"""🚫 Why list.copy() Lies
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

data = {'a': [1, 2], 'b': [3, 4]}
# TODO: create a deep copy of data named safe
safe = data.copy()
safe['a'][0] = 99


# ---- SOLUTION (peek only after trying!) ----
# import copy
# original = [[1, 2], [3, 4]]
# deep = copy.deepcopy(original)
# deep[0][0] = 99
# print(original)  # [[1, 2], [3, 4]]
