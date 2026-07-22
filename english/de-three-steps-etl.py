"""Every data pipeline is just 3 steps 🔧
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

# TODO: write a load() that appends rows into a list called warehouse


# ---- SOLUTION (peek only after trying!) ----
# def extract(): return [{"name": " alice ", "age": "30"}]
# def transform(rs): return [{"name": r["name"].strip().title(), "age": int(r["age"])} for r in rs]
# def load(rs, wh): wh.extend(rs); return wh
# 
# wh = []
# load(transform(extract()), wh)
# print(wh)
# # [{'name': 'Alice', 'age': 30}]
