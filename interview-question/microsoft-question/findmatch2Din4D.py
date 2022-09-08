"""
PRACTICE -> Search a Word in a 2D Grid of characters
https://www.geeksforgeeks.org/check-if-a-word-exists-in-a-grid-or-not/

Dada uma grade 2D de caracteres e uma palavra, a tarefa é verificar se essa palavra existe ou não na grade.
Uma palavra pode ser correspondida em 4 direções a qualquer momento.
As 4 direções são: horizontalmente esquerda e direita, verticalmente para cima e para baixo.

Source: Microsoft Interview.

Input:  grid[][] = {"axmy",
                    "bgdf",
                    "xeet",
                    "raks"};
Output: Yes

a x m y
b (g) d f
x (e) (e) t
ra (k)  (s)

Input: grid[][] = {"axmy",
                   "brdf",
                   "xeet",
                   "rass"};
Output : No
"""

r = 4
c = 4


# Function to check if a word exists in a grid starting from the first match in the grid level: index till
# which pattern is matched x, y: current position in 2D array

def findmatch(mat, pat, x, y, nrow, ncol, level):
    l = len(pat)

    # Pattern matched  
    if level == l:
        return True

    # Out of Boundary  
    if x < 0 or y < 0 or x >= nrow or y >= ncol:
        return False

    # If grid matches with a letter while recursion
    if mat[x][y] == pat[level]:

        # Marking this cell as visited  
        temp = mat[x][y]
        mat[x].replace(mat[x][y], "#")

        # Finding subpattern in 4 directions
        res = (findmatch(mat, pat, x - 1, y, nrow, ncol, level + 1) |
               findmatch(mat, pat, x + 1, y, nrow, ncol, level + 1) |
               findmatch(mat, pat, x, y - 1, nrow, ncol, level + 1) |
               findmatch(mat, pat, x, y + 1, nrow, ncol, level + 1))

        # Marking this cell as unvisited again
        mat[x].replace(mat[x][y], temp)
        return res

    else:  # Not matching then false
        return False


# Function to check if the word exists in the grid or not
def checkMatch(mat, pat, nrow, ncol):
    l = len(pat)

    # If total characters in matrix is less then pattern lenghth
    if l > nrow * ncol:
        return False

    # Traverse in the grid  
    for i in range(nrow):
        for j in range(ncol):

            # If first letter matches, then recur and check
            if mat[i][j] == pat[0]:
                if findmatch(mat, pat, i, j, nrow, ncol, 0):
                    return True
    return False


# Driver Code  
if __name__ == "__main__":

    grid = ["axmy",
            "brdf",
            "xeet",
            "rass"]

    # Function to check if word exists or not
    if checkMatch(grid, "geeks", r, c):
        print("Yes")
    else:
        print("No")

    # This code is contributed by Ryuga
