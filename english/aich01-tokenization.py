# AI From Scratch — Chapter 1: Tokenization (CORRECTED)
# Fix (2026-07-14): ID 0 is now reserved for <UNK>, so unknown words are flagged
# instead of silently becoming a real word. Run this and try your own unknown words.

class TinyTokenizer:
    def __init__(self, text):
        self.tokens = text.split()
        self.vocab = sorted(set(self.tokens))
        self.w2i = {"<UNK>": 0}
        for i, w in enumerate(self.vocab):
            self.w2i[w] = i + 1
        self.i2w = {i: w for w, i in self.w2i.items()}
    def encode(self, text):
        return [self.w2i.get(t, 0) for t in text.split()]   # 0 = <UNK>
    def decode(self, ids):
        return " ".join(self.i2w.get(i, "<UNK>") for i in ids)

tok = TinyTokenizer("hello world hello python")
print("Class Encoded:", tok.encode("hello python cat"))

# --- try it: unknown words become <UNK>, not a real word ---
tok = TinyTokenizer("the cat sat on the mat")
ids = tok.encode("the cat jumped")   # "jumped" is unknown -> <UNK>
print("Input: the cat jumped -> IDs:", ids)
print("Decoded back:", tok.decode(ids))

# TODO: add an `encode` call with TWO unknown words and confirm BOTH show as 0 (<UNK>),
#       then decode the result and check both print as "<UNK>".
