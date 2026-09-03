"""Class Variable Leak 😱
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

class Cat:
    def __init__(self): self.sounds = []
c1 = Cat(); c1.sounds.append('meow'); c2 = Cat()
# TODO: print(c2.sounds)


# ---- SOLUTION (peek only after trying!) ----
# class Dog:
#     def __init__(self): self.tricks = []
# d1 = Dog(); d1.tricks.append('roll')
# d2 = Dog()
# print(d2.tricks)  # []
