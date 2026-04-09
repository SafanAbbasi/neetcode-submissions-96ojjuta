class Solution:
    def trap(self, height: List[int]) -> int:
        # to trap you need the minumum of the heights of left and right 
        # increment the smaller height
        # need to figure out when to add to total water
        # trapped is min(hleft,hright) - height[i] where i would have to be less than that to trap water



        left, right = 0, len(height) -1
        leftMax = height[left]
        rightMax = height[right]

        total = 0

        while left < right:

            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if leftMax < rightMax: 
                total += (min(leftMax,rightMax) - height[left] )
                left += 1
            else:
                total += (min(leftMax,rightMax) - height[right] )
                right -= 1
            
        return total