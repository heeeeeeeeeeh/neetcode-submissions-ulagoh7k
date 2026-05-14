class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        row = None
        while l <= r:
            row = l + (r-l)//2

            if matrix[row][0] <= target and matrix[row][-1] >= target:
                break
            elif  matrix[row][0] > target:
                r = row - 1
            else:
                l = row + 1
        if r < l:
            return False
        l, r = 0, len(matrix[0])-1
        while l <= r:
            mid = l + (r-l)//2
            num = matrix[row][mid]
            
            if num == target:
                return True
            elif num > target:
                r = mid - 1
            else:
                l = mid + 1
        return False