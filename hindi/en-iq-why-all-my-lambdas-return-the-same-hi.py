"""सारे Lambdas Same क्यों Match करते हैं? 😱
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

fs = [lambda: n * 2 for n in range(3)]
# TODO: make each function keep its own n
print([f() for f in fs])


# ---- SOLUTION (peek only after trying!) ----
# fs = [lambda i=i: i for i in range(3)]
# print([f() for f in fs])  # [0, 1, 2]
