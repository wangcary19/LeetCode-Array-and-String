# February 1st, 2024
def getRow(self, rowIndex: int) -> List[int]:
    if rowIndex == 0:
        return [1]
    elif rowIndex == 1:
        return [1, 1]
    else:
        row = [1, 1]
        for r in range(1, rowIndex):
            for i in range(len(row) - 1, 0, -1):
                row[i] = row[i] + row[i - 1]
            # end-for
            row.append(1)
        # end-for
        return row