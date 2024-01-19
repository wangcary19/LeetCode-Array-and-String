# January 18th, 2024
def strStr(self, haystack: str, needle: str) -> int:
    for i in range(0, len(haystack)):
        if haystack[i:i + len(needle)] == needle:
            return i
    # end-for
    return -1