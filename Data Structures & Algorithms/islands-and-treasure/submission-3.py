class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))

        def bfs():
            dist = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    addNeighCells(row, col)
                    grid[row][col] = dist
                dist += 1
        
        def addNeighCells(row, col):
            if row > 0 and grid[row-1][col] != -1:
                addCell(row-1, col)
            if row < len(grid)-1 and grid[row+1][col] != -1:
                addCell(row+1, col)
            if col > 0 and grid[row][col-1] != -1:
                addCell(row, col-1)
            if col < len(grid[0])-1 and grid[row][col+1] != -1:
                addCell(row, col+1)
        
        def addCell(row, col):
            if (row,col) in visited: return
            visited.add((row, col))
            q.append((row, col))
        bfs()
