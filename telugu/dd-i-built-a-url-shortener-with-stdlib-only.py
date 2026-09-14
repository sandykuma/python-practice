"""Stdlib లో URL Shortener 🔗
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

import hashlib; db={}
def shorten(u): k=hashlib.md5(u.encode()).hexdigest()[:6]; db[k]=u; return k
# TODO: write resolve(k) to fetch url


# ---- SOLUTION (peek only after trying!) ----
# import base64; counter=0; db={}
# def shorten(url): global counter; key=base64.urlsafe_b64encode(counter.to_bytes(2,'big')).decode().rstrip('='); counter+=1; db[key]=url; return key
# def resolve(key): return db.get(key)
# print(shorten("https://example.com")) # AA
