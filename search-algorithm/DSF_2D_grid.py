"""
Pesquisa em profundidade (DFS - Depth-first search)
DFS para verificar se existem caracteres nas diagonais na grade 2D
"""

board = [
    ['Z', 'B', 'N', 'O', 'N', 'O'],
    ['Z', 'B', 'O', 'N', 'N', 'Z'],
    ['B', 'O', 'B', 'B', 'N', 'B'],
    ['O', 'N', 'O', 'N', 'N', 'N'],
    ['Z', 'Z', 'Z', 'Z', 'B', 'O'],
    ['B', 'Z', 'O', 'Z', 'B', 'N']
]


def dfs(board, word):
    if not board:
        return False

    n, m = len(board), len(board[0])
    stack = []

    for i in range(n):
        for j in range(m):
            if board[i][j] == word[0]:
                stack.append((i, j, 0, {(i, j)}))

    while stack:
        i, j, step, visit = stack.pop()
        step += 1

        if step == len(word):
            return True

        # 8 neighbors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        for ni, nj in [(i + x, j + y) for x, y in directions]:
            if (ni, nj) not in visit and 0 <= ni < n and 0 <= nj < m and board[ni][nj] == word[step]:
                stack.append((ni, nj, step, visit.union({(ni, nj)})))

    return False


print(dfs(board, "ZZBO"))  # => True
print(dfs(board, "NBNZ"))  # => True
print(dfs(board, "BNZO"))  # => True
print(dfs(board, "ZBN"))  # => True
print(dfs(board, "ZBNN"))  # => True
