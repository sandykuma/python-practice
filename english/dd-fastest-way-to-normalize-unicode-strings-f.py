"""⚡ Normalize Unicode Fast
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

import unicodedata
s1 = 'Ångström'                 # precomposed
s2 = 'A\u030Angstro\u0308m'   # same text, decomposed
# TODO: show s1 == s2 is False, then normalize both with NFC and compare again


# ---- SOLUTION (peek only after trying!) ----
# import unicodedata
# s1 = 'café'
# s2 = 'cafe\u0301'
# print(unicodedata.normalize('NFC', s1) == unicodedata.normalize('NFC', s2))
# # True
