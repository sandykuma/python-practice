"""Two Sum: From Brute Force to One Pass
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

nums = [3, 2, 4]
target = 6
# TODO: return the two indices that add to target


# ---- SOLUTION (peek only after trying!) ----
# def two_sum(nums, target):
#     seen = {}
#     for i, number in enumerate(nums):
#         needed = target - number
#         if needed in seen:
#             return [seen[needed], i]
#         seen[number] = i
#     return []
# 
# print(two_sum([2, 7, 11, 15], 9))
