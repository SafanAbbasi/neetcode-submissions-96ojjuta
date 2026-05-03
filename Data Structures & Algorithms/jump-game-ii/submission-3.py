
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


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res