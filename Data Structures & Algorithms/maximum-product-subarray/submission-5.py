class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i] = maximum subarray to this point? 

        # final answer will return dp[len(nums)]
        # dp[0] = 1 base case so that dp[1] is just max(dp[i], dp[i-1] * dp[i]) where i = 1

        max_prod = min_prod = 1
        res = float('-inf')
        max_prod = 1
        min_prod = 1

        for n in nums:
            temp = max_prod
            max_prod = max(max_prod * n, min_prod * n, n)
            min_prod = min(temp * n, min_prod * n, n)
            res = max(res, max_prod)

        return res
        

# other problem which is Kadane's algo

        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

        return max(dp)


        max_sum = nums[0]
        curr = 0

        for n in nums:
            curr = max(curr + n, n)  # extend or start fresh
            max_sum = max(max_sum, curr)

        return max_sum