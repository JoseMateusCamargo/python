"""
PRACTICE -> Search a Word in a 2D Grid of characters
https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/

Dada uma grade 2D de caracteres e uma palavra, encontre todas as ocorrências dessa palavra na grade. Uma palavra
pode ser correspondida nas 8 direções a qualquer momento. Diz-se que a palavra é encontrada em uma direção
se todos os caracteres corresponderem nessa direção (não na forma de zig-zag).
As 8 direções são: Horizontalmente à esquerda, Horizontalmente à direita, Verticalmente para cima e
4 direções em diagonal.

Source: Microsoft Interview Question.

Input:  grid[][] = {"GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
        word = "GEEKS"

Output: pattern found at 0, 0
        pattern found at 0, 8
        pattern found at 1, 0

Explanation: 'GEEKS' can be found as prefix of 1st 2 rows and suffix of first row

Input:  grid[][] = {"GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
        word = "EEE"

Output: pattern found at 0, 2
        pattern found at 0, 10
        pattern found at 2, 2
        pattern found at 2, 12

Explanation: EEE can be found in first row twice at index 2 and index 10and in second row at 2 and 12
"""


class GFG:

    def __init__(self):
        self.R = None
        self.C = None
        self.dir = [[-1, 0], [1, 0], [1, 1], [1, -1], [-1, -1], [0, 1], [0, -1]]

        # This function searches in all 8-direction from point(row, col) in grid[][]

    def search2D(self, grid, row, col, word):

        # If first character of word doesn't match with the given starting point in grid.
        if grid[row][col] != word[0]:
            return False

        # Search word in all 8 directions starting from (row, col)
        for x, y in self.dir:

            # Initialize starting point for current direction
            rd, cd = row + x, col + y
            flag = True

            # First character is already checked, match remaining characters
            for k in range(1, len(word)):

                # If out of bound or not matched, break 
                if (0 <= rd < self.R and
                        0 <= cd < self.C and
                        word[k] == grid[rd][cd]):

                    # Moving in particular direction 
                    rd += x
                    cd += y
                else:
                    flag = False
                    break

            # If all character matched, then value of flag must be false
            if flag:
                return True
        return False

    # Searches given word in a given matrix in all 8 directions
    def patternSearch(self, grid, word):

        # Rows and columns in given grid 
        self.R = len(grid)
        self.C = len(grid[0])

        # Consider every point as starting point and search given word
        for row in range(self.R):
            for col in range(self.C):
                if self.search2D(grid, row, col, word):
                    print("pattern found at " +
                          str(row) + ', ' + str(col))

                # Driver Code


if __name__ == '__main__':
    grid = ["GEEKSFORGEEKS",
            "GEEKSQUIZGEEK",
            "IDEQAPRACTICE"]

    gfg = GFG()
    gfg.patternSearch(grid, 'GEEKS')
    print('')
    gfg.patternSearch(grid, 'EEE')

# This code is contributed by Yezheng Li
