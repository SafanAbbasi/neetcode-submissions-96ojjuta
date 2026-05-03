class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsum = nums[0]
        currsum = 0
        for num in nums:
            
            if currsum < 0:
                currsum = num
            else:
                currsum += num
            
            maxsum = max(maxsum, currsum)

        return  maxsum
