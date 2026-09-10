"""Default dict भूल जाता है डिलीट की हुई keys 😱
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

from collections import defaultdict
dd = defaultdict(int)
dd['x'] = 5
del dd['x']
# TODO: access dd['x'] and print the result


# ---- SOLUTION (peek only after trying!) ----
# from collections import defaultdict
# dd = defaultdict(list)
# dd['a'].append(1)
# del dd['a']
# print(dd['a'])  # []
