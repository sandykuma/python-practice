"""Python Decorators అంటే ఏంటి? 🪄
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

def bold_text(func):
    def wrapper():
        # TODO: Print '<b>' then call func() then print '</b>'
        pass
    return wrapper


# ---- SOLUTION (peek only after trying!) ----
# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper
# 
# @my_decorator
# def say_hi():
#     print("Hi there!")
# 
# say_hi()
# # Before function call
# # Hi there!
# # After function call
