# January 18th, 2024

def longestCommonPrefix(self, strs: List[str]) -> str:
    commons = strs[0]
    if len(strs) == 1:
        return commons
    elif len(commons) == 0:
        return ""
    else:
        for s in range(1, len(strs)):
            comparator = strs[s]

            for x in range(0, len(commons)):
                if x < len(comparator):
                    if commons[x] != comparator[x]:
                        commons = commons[0:x]
                        break
                    else:
                        continue
                else:
                    commons = commons[0:x]
                    break

        return commons