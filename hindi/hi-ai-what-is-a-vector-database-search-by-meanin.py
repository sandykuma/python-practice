"""Vector DB का जादू ✨
Practice: complete the TODO below, then run the file.
From the Python Shorts channel — subscribe for one concept a day!
"""

# दो बिंदुओं की लिस्ट बनाओ
points = [[10,10],[20,20],[30,30]]
query = [25,25]
# TODO: numpy या लिस्ट‑कॉम्प्रिहेंशन से nearest neighbour ढूँढो और प्रिंट करो


# ---------------- SOLUTION (peek only after trying!) ----------------
# import numpy as np
# points = np.array([[1,2],[3,4],[5,6]])
# query = np.array([2,3])
# # vectorized distance & argmin
# idx = np.argmin(((points - query)**2).sum(axis=1))
# print(points[idx])  # [1 2]
