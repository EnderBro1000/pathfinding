def minWithNone(a, b): # returns the min between a and b, or whichever is not None
    if a is None:
        return b
    elif b is None:
        return a
    return min(a,b)
    
def maxWithNone(a, b): # returns the max between a and b, or whichever is not None
    if a is None:
        return b
    elif b is None:
        return a
    return max(a,b)

def matrixString(mat) -> str:
    out = ""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            out += f"{mat[i][j]} "
        out += "\n"
    return out