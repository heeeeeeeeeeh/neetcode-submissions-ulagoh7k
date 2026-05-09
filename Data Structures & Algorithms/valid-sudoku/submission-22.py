class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = defaultdict(set)

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                
                if ( num in rows[row] or
                     num in cols[col] or
                     num in boxes[(row//3,col//3)]):
                     return False
                rows[row].add(num)
                cols[col].add(num)
                boxes[(row//3,col//3)].add(num)
        return True
        