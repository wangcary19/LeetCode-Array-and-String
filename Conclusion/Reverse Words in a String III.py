# February 1st, 2024

def reverseWords(self, s: str) -> str:
    return " ".join([x[::-1] for x in s.split()])