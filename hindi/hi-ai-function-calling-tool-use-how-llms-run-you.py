"""LLM को फ़ंक्शन चलाने दो! 🚀
Practice: complete the TODO below, then run the file.
From the Python Shorts channel — subscribe for one concept a day!
"""

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

dispatch = {'sub': sub, 'div': div}
op = 'sub'
# TODO: Use dispatch dict to call the correct function with arguments 10 and 3 and print result


# ---------------- SOLUTION (peek only after trying!) ----------------
# def add(a,b):
#     return a+b
# 
# def mul(a,b):
#     return a*b
# 
# dispatch = {'add': add, 'mul': mul}
# op = 'add'
# print(dispatch[op](3,4))  # 7
