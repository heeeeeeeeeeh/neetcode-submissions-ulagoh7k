class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        boxes = [set() for _ in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board)):
                num = board[row][col]
                box_index = (row // 3 * 3) + (col // 3)
                if num == ".":
                    continue
                if num in rows[row] or num in cols[col] or num in boxes[box_index]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                boxes[box_index].add(num)
        return True