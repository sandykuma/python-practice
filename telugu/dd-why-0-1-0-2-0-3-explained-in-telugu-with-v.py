"""0.1 + 0.2 ≠ 0.3 🤔
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

# TODO: Format the sum to show exactly two decimal places
s = 0.1 + 0.2
print(f"{s:.2f}")


# ---- SOLUTION (peek only after trying!) ----
# from decimal import Decimal, getcontext
# getcontext().prec = 10
# result = Decimal('0.1') + Decimal('0.2')
# print(result)  # 0.3
