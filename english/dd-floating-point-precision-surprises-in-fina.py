"""💰 Float Pitfall in Money Math
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

price = 0.10
qty = 3
total = price * qty  # TODO: use Decimal for exact cents
print(total)


# ---- SOLUTION (peek only after trying!) ----
# from decimal import Decimal
# total = Decimal('0.1') + Decimal('0.2')
# print(total)  # 0.3
