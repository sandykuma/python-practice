"""Nested List Comprehension అంటే ఏంటి? 🤔
Practice: complete the TODO below, then run the file.
From the Python Shorts channel — subscribe for one concept a day!
"""

matrix = [[1, 2], [3, 4]]
# TODO: Create a list of all individual numbers from matrix using nested list comprehension
result = [num for sublist in matrix for num in sublist]
print(result)


# ---------------- SOLUTION (peek only after trying!) ----------------
# items = [1, 2, 3]
# # Pythonic way: Nested List Comprehension
# result = [(i, j) for i in items for j in range(3)]
# 
# print(result) # [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)]
