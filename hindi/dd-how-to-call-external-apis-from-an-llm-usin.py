"""एपीआई कॉल एक लाइन में 🚀
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

import requests
def get_baz():
    return requests.get('https://httpbin.org/get?baz=qux').json()['args']['baz']
# TODO: print the result


# ---- SOLUTION (peek only after trying!) ----
# import requests
# def get_foo():
#     return requests.get('https://httpbin.org/get?foo=bar').json()['args']['foo']
# print(get_foo())
# # bar
