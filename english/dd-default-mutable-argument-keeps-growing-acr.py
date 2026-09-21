"""Stop Using [] as Default! 🐛
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

def log(msg, logs=[]):
    logs.append(msg)
    return logs
# TODO: Fix the mutable default so each call starts fresh


# ---- SOLUTION (peek only after trying!) ----
# def add_item(item, cart=None):
#     if cart is None: cart = []
#     cart.append(item); return cart
# print(add_item("apple")); print(add_item("banana"))
# # ['apple']\n['banana']
