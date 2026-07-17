"""Reverse Strings 😲 Keep Surrogates
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

strings = ["😀ab", "cd😀"]
# TODO: replace this with surrogate‑safe reversal for each string
result = [s[::-1] for s in strings]


# ---- SOLUTION (peek only after trying!) ----
# import struct
# s = "😀ab"
# us = struct.unpack('<'+'H'*(len(s.encode('utf-16-le'))//2), s.encode('utf-16-le'))
# rev = struct.pack('<'+'H'*len(us), *us[::-1]).decode('utf-16-le')
# print(rev)  # ba😀
