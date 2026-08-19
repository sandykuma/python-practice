"""Shallow Copy Trap 😱
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

grid = [[5,6],[7,8]]
# TODO: create a deep copy without copy.deepcopy
dup = [row[:] for row in grid]
dup[0][1] = 0
print(grid)


# ---- SOLUTION (peek only after trying!) ----
# import copy
# original = [[1,2],[3,4]]
# deep = copy.deepcopy(original)
# deep[0][0] = 99
# print(original)  # [[1, 2], [3, 4]]
