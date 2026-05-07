class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            index = self.binarySearch(row, target)
            if index != -1:
                return True
        return False
    def binarySearch(self, row, target):
        l, r = 0,len(row)-1

        while l <= r:
            mid = l + (r-l//2)
            if row[mid] == target:
                return mid
            elif row[mid] > target:
                r = mid - 1
            else:
                l  = mid + 1
        return -1