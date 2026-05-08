class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # every number can be a postive or negative number essentially

        memo = {}
        

        def dfs(i,total):

            if i >= len(nums) and total == target:
                return 1
            # if total > target:
            #     return 0
            if i >= len(nums):
                return 0

            
            # choice 1 keep positive and add

            plusadd = dfs(i+1,total + nums[i])

            negativeadd = dfs(i+1, total - nums[i])

            return plusadd + negativeadd

        return dfs(0,0)