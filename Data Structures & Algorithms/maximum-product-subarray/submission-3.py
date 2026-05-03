class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i] = maximum subarray to this point? 

        # final answer will return dp[len(nums)]
        # dp[0] = 1 base case so that dp[1] is just max(dp[i], dp[i-1] * dp[i]) where i = 1

        dp = [float("-inf")] * (len(nums) + 1)
        dp[0] = 1
        max_prod = 1
        min_prod = 1

        for i in range(1,len(nums)+1):
            dp[i] = max(min_prod * nums[i-1], max_prod * nums[i-1], nums[i-1])
            temp = max_prod  # save before overwriting!
            max_prod = max(max_prod * nums[i-1], min_prod * nums[i-1], nums[i-1])
            min_prod = min(temp * nums[i-1], min_prod * nums[i-1], nums[i-1])

        
        return max(dp[1:])