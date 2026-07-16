"""Deep Copy Lists 🚀
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

def deep_copy(obj):
    if isinstance(obj, list):
        return [deep_copy(i) for i in obj]
    # TODO: add support for tuples and sets
    return obj


# ---- SOLUTION (peek only after trying!) ----
# def deep_copy(obj):
#     return [deep_copy(i) if isinstance(i, list) else i for i in obj]
# original = [[1, 2], [3, 4]]
# copy = deep_copy(original)
# print(copy)  # [[1, 2], [3, 4]]
