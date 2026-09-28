"""🚫 List * के Unexpected Tricks
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

# Create a 4x4 matrix filled with zeros
matrix = [[0]*4]*4  # TODO: replace this line with a list comprehension
matrix[2][3] = 7
print(matrix)


# ---- SOLUTION (peek only after trying!) ----
# rows = [[0]*3 for _ in range(3)]
# rows[0][0] = 9
# print(rows)  # [[9, 0, 0], [0, 0, 0], [0, 0, 0]]
