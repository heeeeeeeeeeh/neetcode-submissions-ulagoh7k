class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            if i >= len(word):
                return True
            if (r >= ROWS or c >= COLS
                or r < 0 or c < 0
                or board[r][c] != word[i]
                or (r, c) in visited):
                return False
            
            visited.add((r, c))
            res = (dfs(r + 1, c, i + 1)
                    or dfs(r - 1, c, i + 1)
                    or dfs(r, c + 1, i + 1)
                    or dfs(r, c - 1, i + 1))
            visited.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0): return True
        return False