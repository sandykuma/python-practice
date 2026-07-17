"""प्रॉम्प्ट ट्रिक: जवाब दोगुना सटीक! 🚀
Practice: complete the TODO, then run it.
From the coding Shorts channel — subscribe for one concept a day!
"""

def mock_llm(p): return "The capital of France is Paris." if "step by step" in p else "Paris"
# TODO: Build the prompt that asks for capital and includes step-by-step reasoning
prompt = ""
print(mock_llm(prompt))
# The capital of France is Paris.


# ---- SOLUTION (peek only after trying!) ----
# def mock_llm(p): return "The capital of France is Paris." if "step by step" in p else "Paris"
# prompt = "What is the capital of France? Let's think step by step"
# print(mock_llm(prompt))
# # The capital of France is Paris.
