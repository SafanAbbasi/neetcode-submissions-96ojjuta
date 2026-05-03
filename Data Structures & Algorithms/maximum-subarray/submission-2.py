class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsum = nums[0]
        currsum = 0
        for num in nums:
            
            currsum = max(currsum+num, num)
            
            maxsum = max(maxsum, currsum)

        return maxsum
