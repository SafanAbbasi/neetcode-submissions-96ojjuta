class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def robbing(nums):

            rob1 = 0 
            rob2 = 0
            if len(nums) == 1:
                return nums[0]

            for n in nums:
                temp = max(n + rob1, rob2)

                rob1 = rob2
                rob2 = temp

            return rob2

        return max(robbing(nums[1:]), robbing(nums[:-1])) if len(nums) > 1 else nums[0]
