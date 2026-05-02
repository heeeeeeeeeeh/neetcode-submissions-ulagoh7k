class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boards = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                num = board[row][col]
                if num == ".":
                    continue
                
                if num in rows[row] or num in cols[col] or num in boards[(row // 3,col // 3)]:
                    return False
                
                rows[row].add(num)
                cols[col].add(num)
                boards[(row // 3, col // 3)].add(num)
        return True