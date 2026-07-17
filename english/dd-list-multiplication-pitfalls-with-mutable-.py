"""🚫 Don't Multiply Lists Like This!
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

# TODO: fix the matrix creation to avoid shared references
matrix = [[0]*3]*3
matrix[1][2] = 5
print(matrix)


# ---- SOLUTION (peek only after trying!) ----
# rows = [[0]*3 for _ in range(3)]
# rows[0][0] = 9
# print(rows)  # [[9, 0, 0], [0, 0, 0], [0, 0, 0]]
