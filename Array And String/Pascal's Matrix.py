# January 17th, 2024

def generate(self, numRows: int) -> List[List[int]]:
    prev = [1, 1]
    row = []

    out = [[1], [1, 1]]
    c = 2

    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        while c != numRows:

            row.append(1)
            for i in range(0, len(prev) - 1):
                row.append(prev[i] + prev[i + 1])
            # end-for
            row.append(1)

            c += 1
            prev = row
            out.append(row)
            row = []
        # end-while
        return out
    # end-else