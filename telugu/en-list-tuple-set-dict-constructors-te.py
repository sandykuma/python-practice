"""Stop Building Lists Manually! 🚀
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

s = "hi"
# TODO: build list, tuple, set, and dict of char->ord using constructors
lst, tpl, st, dct = list(s), tuple(s), set(s), dict((c, ord(c)) for c in s)


# ---- SOLUTION (peek only after trying!) ----
# data = [1, 2]
# pairs = [(1, 'a'), (2, 'b')]
# print(list(data), tuple(data), set(data), dict(pairs))
# # [1, 2] (1, 2) {1, 2} {1: 'a', 2: 'b'}
