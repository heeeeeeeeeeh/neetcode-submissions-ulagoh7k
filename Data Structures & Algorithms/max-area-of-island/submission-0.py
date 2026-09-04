class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            area = 1  # count the starting cell

            while q:
                currentR, currentC = q.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nextR, nextC = currentR + dr, currentC + dc
                    if nextR < 0 or nextC < 0 or nextR >= ROWS or nextC >= COLS:
                        continue
                    if grid[nextR][nextC] == 1:
                        q.append((nextR, nextC))
                        grid[nextR][nextC] = 0
                        area += 1
            return area

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)
        return maxArea