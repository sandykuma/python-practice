"""Turn Words into Numbers 🔢
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

sentence_a = "apple orange"
sentence_b = "orange banana"
# TODO: build bag‑of‑words vectors and compute cosine similarity


# ---- SOLUTION (peek only after trying!) ----
# import math
# 
# def cosine(a, b):
#     dot = sum(x*y for x, y in zip(a, b))
#     norm_a = math.sqrt(sum(x*x for x in a))
#     norm_b = math.sqrt(sum(y*y for y in b))
#     return dot / (norm_a * norm_b)
# 
# vec1 = [1, 0, 1]
# vec2 = [0, 1, 1]
# print('Cosine similarity:', round(cosine(vec1, vec2), 3))  # Cosine similarity: 0.5
