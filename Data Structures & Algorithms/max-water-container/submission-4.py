class Solution:
    #Understand: find the two bars that can hold most area. 
    #Plan:
    # init left pointer to point to first element
    # init right pointer to point to last element
    # while left less than right-1 
        # if the element to the right of left pointer is bigger than left pointer
            # update left pointer to next element
        # else if the element to the left of right pointer is bigger than right pointer
            # update right pointer to previous element
    # calculate max area by 
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        res = 0

        while left < right:
            area = min(heights[left],heights[right])*(right-left)
            res = max(area,res)
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return res