"""🚫 Slice Copy का जाल
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

matrix = [[1, 2], [3, 4]]
copy_mat = matrix[:]  # TODO: make a copy that doesn't share inner lists
copy_mat[0][0] = 99
print(matrix)  # Should show original unchanged


# ---- SOLUTION (peek only after trying!) ----
# a = [[1,2],[3,4]]
# b = [row[:] for row in a]
# b[0][0] = 99
# print(a)
# # [[1, 2], [3, 4]]
