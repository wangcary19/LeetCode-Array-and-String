# February 1st, 2024
def reverseWords(self, s: str) -> str:
    l = s.split()
    l = reversed(l)
    j = " ".join(l)
    return j