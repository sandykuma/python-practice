"""Stop Comparing Raw Strings 🧹
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

import unicodedata
word1 = 'naïve'
word2 = 'naive\u0308'
# TODO: normalize both to NFD and print if they match


# ---- SOLUTION (peek only after trying!) ----
# import unicodedata
# s1 = 'café'
# s2 = 'cafe\u0301'
# print(unicodedata.normalize('NFC', s1) == unicodedata.normalize('NFC', s2))  # True
