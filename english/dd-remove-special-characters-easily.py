"""Stop wasting time cleaning strings! 🚀
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

import re\n\ntext = "Hello! @World"
# TODO: Replace all symbols with an empty string using re.sub()
clean_text = re.sub(r'[^a-zA-Z0-9]', '', text)
print(clean_text)


# ---- SOLUTION (peek only after trying!) ----
# import re
# 
# text = "Hello, World! @123"
# # Use a regex replace to strip everything except letters and numbers
# clean_text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
# print(clean_text)
