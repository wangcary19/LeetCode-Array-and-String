# February 1st, 2024

def reverseWords(self, s: str) -> str:
    out = ""
    for i in range(len(s) - 1, -1, -1):
        out += s[i]
    l = out.split()
    l = reversed(l)
    j = " ".join(l)
    return j