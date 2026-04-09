class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        # -4, -1, -1, 0, 1, 2 



        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right: 
                pair_total = nums[left] + nums[right]
                if pair_total == -nums[i]:
                    res.append([ nums[i], nums[left], nums[right] ] )
                    while left + 1 < len(nums) and nums[left+1] == nums[left]:
                        left += 1
                    while right-1 >= 0 and nums[right-1] == nums[right]:    
                        right -= 1

                    left += 1 
                    right -= 1
                    
                elif pair_total > -nums[i]:
                    right -= 1
                else:
                    left += 1
        
        return res