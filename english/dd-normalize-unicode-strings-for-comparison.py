"""Fix Unicode Comparison 🔤
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

import unicodedata
a = "Stra\u00dfe"
b = "Strasse"
# TODO: normalize both strings to NFD and check if they are equal


# ---- SOLUTION (peek only after trying!) ----
# import unicodedata
# s1 = "café"
# s2 = "cafe\u0301"
# print(unicodedata.normalize('NFC', s1) == unicodedata.normalize('NFC', s2))  # True
