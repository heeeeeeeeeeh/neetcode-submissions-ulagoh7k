class Solution:
    #Understand: check if sudoku board is vaild
    #Plan:
    #row validation
        #loop though row in board
            # init a hash for prev numbers in row
            #loop though each col in board
                # if current number is in prev number hash and not . return false
                # else put cur num in hashmap
    # col validation
        #loop though row in board
            #loop though col in board
                # if current number is not . and is in prev number
                    # return false
                # else 
                    # put cur num in hashmap
    # loop though each row of SubBoards 
        # loop though col of subboards
            # loop though subboard row
                # loop though each subboard col
                    # init hash for prev numbers in subboard
                    # loop though each col
                        # if current number is in prev num
                            # else put cur num in hashmap
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".": 
                    continue
                boxIndex = (row // 3) * 3 + (col // 3)
                if  (num in rows[row] or num in cols[col] or num in boxes[boxIndex]):
                    return False
                rows[row].add(num)
                cols[col].add(num)
                boxes[boxIndex].add(num)
        return True