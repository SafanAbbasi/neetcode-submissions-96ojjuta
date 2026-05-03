class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1 = 0 
        rob2 = 0
        if len(nums) == 1:
            return nums[0]

        for n in nums[:-1]:
            temp = max(n + rob1, rob2)

            rob1 = rob2
            rob2 = temp


        rob3 = 0 
        rob4 = 0
        for n in nums[1:]:
            temp = max(n + rob3, rob4)

            rob3 = rob4
            rob4 = temp

        return max(rob2, rob4)