"""🚫 .copy() Lies! Use Deep Copy
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

original = [[1, 2], [3, 4]]
safe = original.copy()  # TODO: replace with deep copy
safe[0][0] = 99
print(original)  # Expected: [[1, 2], [3, 4]]


# ---- SOLUTION (peek only after trying!) ----
# import copy
# orig = [[1,2],[3,4]]
# deep = copy.deepcopy(orig)
# deep[0][0] = 99
# print(orig)  # [[1, 2], [3, 4]]
