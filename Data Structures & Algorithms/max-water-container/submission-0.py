class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area is min of the left and right height * distance between them
        # area = min(hleft, hright) * r - l

        left, right = 0, len(heights) - 1

        maxArea = 0
        while left < right:

            area = min(heights[left], heights[right]) * (right - left)
            
            maxArea = max(maxArea, area)

            # have to decide which pointer to move. whichever one has the smallest height

            if heights[left] <= heights[right]:
                left += 1
            else: 
                right -= 1

        return maxArea
