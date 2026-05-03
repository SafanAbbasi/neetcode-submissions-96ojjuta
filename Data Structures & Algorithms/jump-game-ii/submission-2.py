
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        max_reach = 0
        min_jumps = 0
        current_end = 0  # end of current level

        if len(nums) == 1:
            return 0

        for idx, num in enumerate(nums):

            max_reach = max(max_reach, idx + num)
            if idx == current_end:
                min_jumps += 1
                current_end = max_reach

            if current_end >= (len(nums) -1):
                break
        return min_jumps