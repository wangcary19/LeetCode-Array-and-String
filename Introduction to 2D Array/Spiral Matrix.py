# January 17th, 2023

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

    m = len(matrix)  # height
    n = len(matrix[0])  # width
    s = m * n

    direction = "E"
    bounds = {"nb": 0, "eb": n - 1, "sb": m - 1, "wb": 0}
    i = 0
    j = 0

    out = []

    while len(out) != s:

        out.append(matrix[i][j])

        if direction == "E":  # Going East
            if j == bounds["eb"]:  # at end, kick to South and increase northern bound
                direction = "S"
                bounds["nb"] += 1
                i += 1
            else:  # keep going East
                j += 1
        elif direction == "S":  # Going South
            if i == bounds["sb"]:  # at end, kick to West and decrease eastern bound
                direction = "W"
                bounds["eb"] -= 1
                j -= 1
            else:  # keep going West
                i += 1
        elif direction == "W":  # Going West
            if j == bounds["wb"]:  # at end, kick to North and decrease southern bound
                direction = "N"
                bounds["sb"] -= 1
                i -= 1
            else:  # keep going West
                j -= 1
        else:  # Going North
            if i == bounds["nb"]:  # at end, kick to East and increase western bound
                direction = "E"
                bounds["wb"] += 1
                j += 1
            else:  # continue going North
                i -= 1
    # end-while

    return out