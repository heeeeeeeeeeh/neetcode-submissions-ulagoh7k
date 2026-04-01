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
        for row in range(len(board)):
            preNum = {}
            for col in range(len(board[row])):
                curNum = board[row][col]
                if curNum != "." and curNum in preNum:
                    return False
                else:
                    preNum[curNum] = True

        for col in range(len(board)):
            preNum = {}
            for row in range(len(board)):
                curNum = board[row][col]
                if curNum != "." and curNum in preNum:
                    return False
                else:
                    preNum[curNum] = True
        
        for subboardRow in range(0,9,3):
            print(f"Subboard row: {subboardRow}")
            for subboardCol in range(0,9,3):
                print(f"\tSubboard col: {subboardCol}")
                preNum = {}
                for row in range(3):
                    print(f"\t\tBoard row: {subboardRow+row}")
                    for col in range(3):
                        print(f"\t\t\tBoard col: {subboardCol+col}")
                        curNum = board[subboardRow+row][subboardCol+col]
                        if curNum != "." and curNum in preNum:
                            return False
                        else:
                            preNum[curNum] = True
        return True