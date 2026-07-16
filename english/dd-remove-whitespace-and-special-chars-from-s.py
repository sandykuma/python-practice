"""Clean Strings Fast 🚀
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

import re; s = "Test@# String 123!"
# TODO: replace the pattern to keep only letters
cleaned = re.sub(r'_____', '', s)
print(cleaned)


# ---- SOLUTION (peek only after trying!) ----
# import re
# s = "Hello, World! 123"
# clean = re.sub(r'[^A-Za-z0-9]+', '', s)
# print(clean)  # HelloWorld123
