"""Deep Copy Lists 🚀
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

def deep_copy(obj):
    # TODO: recursively copy lists and dicts
    return [deep_copy(i) for i in obj] if isinstance(obj, list) else {k: deep_copy(v) for k, v in obj.items()} if isinstance(obj, dict) else obj


# ---- SOLUTION (peek only after trying!) ----
# def deep_copy(lst): return [deep_copy(i) if isinstance(i, list) else i for i in lst]
# orig = [[1,2],[3,4]]
# cpy = deep_copy(orig)
# print(cpy)  # [[1, 2], [3, 4]]
