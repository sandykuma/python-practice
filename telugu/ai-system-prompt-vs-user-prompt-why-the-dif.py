"""Prompt Roles Explained 🚀
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

messages = [
    {"role": "system", "content": "You are a friendly tutor."},
    {"role": "user",   "content": "Explain photosynthesis."},
    # TODO: add an assistant reply that summarizes the explanation
]


# ---- SOLUTION (peek only after trying!) ----
# messages = [
#     {"role": "system", "content": "You are a helpful assistant that speaks like a pirate."},
#     {"role": "user",   "content": "Tell me why the sky is blue."},
#     {"role": "assistant", "content": "Arr! The sky looks blue because..."}
# ]
# for m in messages:
#     print(f"{m['role'].title()}: {m['content']}")
# # Output:
# # System: You are a helpful assistant that speaks like a pirate.
# # User: Tell me why the sky is blue.
# # Assistant: Arr! The sky looks blue because...
