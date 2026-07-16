"""⚡ Normalize Unicode Fast
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

import unicodedata
s1 = 'Ångström'
s2 = 'Angstrom\u030A'
# TODO: normalize both and check equality


# ---- SOLUTION (peek only after trying!) ----
# import unicodedata
# s1 = 'café'
# s2 = 'cafe\u0301'
# print(unicodedata.normalize('NFC', s1) == unicodedata.normalize('NFC', s2))
# # True
