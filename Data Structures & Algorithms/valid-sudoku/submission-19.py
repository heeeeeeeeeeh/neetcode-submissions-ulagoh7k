class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                num = board[row][col]
                box_index = (row // 3, col // 3)
                if num == ".":
                    continue
                if num in rows[row] or num in cols[col] or num in boxes[box_index]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                boxes[box_index].add(num)
        return True