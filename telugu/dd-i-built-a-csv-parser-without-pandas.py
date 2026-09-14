"""CSV parse చేయండి pandas లేకుండా 🚀
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

import csv, io
data = "product,price\nApple,10\nBanana,5"
reader = csv.DictReader(io.StringIO(data))
# TODO: convert price to int and print list of dicts


# ---- SOLUTION (peek only after trying!) ----
# import csv, io
# data = "name,age\nAlice,30\nBob,25"
# reader = csv.DictReader(io.StringIO(data))
# rows = list(reader)
# print(rows)  # [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]
