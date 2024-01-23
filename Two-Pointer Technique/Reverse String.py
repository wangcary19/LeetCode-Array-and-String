# January 23rd, 2023

def reverseString(self, s: List[str]) -> None:
    for i in range(0, int(len(s) / 2)):
        s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

def reverseString_alt(self, s: List[str]) -> None:
    s.reverse()