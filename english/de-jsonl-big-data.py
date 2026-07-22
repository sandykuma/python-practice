"""How big data is really stored 📦
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

lines = '{"x": 1}\n{"x": 2}'
# TODO: loop the lines and json.loads each one


# ---- SOLUTION (peek only after trying!) ----
# import json
# # JSONL: one record per line — read it one at a time
# jsonl = '{"id": 1}\n{"id": 2}\n{"id": 3}'
# count = 0
# for line in jsonl.splitlines():
#     record = json.loads(line)
#     count += 1
# print("streamed", count, "records")
# # streamed 3 records
