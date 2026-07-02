"""API Cost Calculator 💰
Practice: complete the TODO below, then run the file.
From the Python Shorts channel — subscribe for one concept a day!
"""

prompt_len = len(prompt.split())
# TODO: Calculate the cost if 100 tokens are priced at 0.05 dollars
cost = prompt_len * 0.05
print(cost)


# ---------------- SOLUTION (peek only after trying!) ----------------
# prompt = "Hello, how are you?"
# # Use a better way to count tokens (approximate)
# tokens_estimate = len(prompt.split())
# cost_estimate = tokens_estimate * 0.0001
# print(f"Cost: {cost_estimate}") # 0.04
