class Solution:
    def rob(self, nums: List[int]) -> int:
        # # dp[i] = max( dp[i-2] + nums[i], dp[i-1] )
        # dp = [0] * len(nums)

        # if not nums:
        #     return 0

        # if len(nums) < 2:
        #     return nums[0]

        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])


        # for i in range(2, len(nums)):
        #     dp[i] = max( dp[i-2] + nums[i], dp[i-1] )


        # return dp[len(nums)- 1]


        rob1 = 0 
        rob2 = 0

        for n in nums:
            temp = max(n + rob1, rob2)

            rob1 = rob2
            rob2 = temp


        return rob2