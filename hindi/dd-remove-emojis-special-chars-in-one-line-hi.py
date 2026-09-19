"""वन-लाइनर इमोजी और सिंबल्स स्ट्रिप करने के लिए 🚀
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

import re
text = "Data🚀Science#2024"
# TODO: write a one‑liner to keep only word characters
print(re.sub(r'[^\w]', '', text))


# ---- SOLUTION (peek only after trying!) ----
# import re
# text = "Hello!🌟World@2024"
# cleaned = re.sub(r'[^\w]', '', text)
# print(cleaned)  # HelloWorld2024
