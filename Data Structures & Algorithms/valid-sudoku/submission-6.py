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

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

        return True