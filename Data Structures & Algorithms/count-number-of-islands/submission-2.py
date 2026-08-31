class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        numI = 0
        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))
            while len(q) > 0:
                currentRow, currentCol = q.popleft()
                for rowOffset, colOffset in [[1,0], [-1,0], [0,1], [0,-1]]:
                    nextRow, nextCol = currentRow + rowOffset, currentCol + colOffset
                    if nextRow < 0 or nextCol < 0 or nextRow == ROWS or nextCol == COLS or grid[nextRow][nextCol] == "0":
                        continue
                    grid[nextRow][nextCol] = "0"
                    q.append((nextRow, nextCol))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    numI += 1
        return numI