class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 # middle index

            if nums[mid] == target:
                return mid
            if nums[mid] < target: 
                # move left inward
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1


        # no target found
        return -1