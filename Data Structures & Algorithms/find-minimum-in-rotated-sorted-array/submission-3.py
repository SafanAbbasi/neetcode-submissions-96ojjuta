class Solution:
    def findMin(self, nums: List[int]) -> int:
        # keep track of when we intersect and order starts from 1

        l, r = 0 , len(nums) - 1
        minval = nums[l]

        while l <= r:
            mid = (l + r) // 2
            if nums[r] > nums[mid]: # still increasing between mid and r
                minval =  min(minval, nums[mid])
                r = mid - 1

            elif nums[l] <= nums[mid]: # still increasing betwee l and mid
                
                minval =  min(minval, nums[mid])
                l = mid + 1
            elif nums[mid] == nums[r]:
                minval =  min(minval, nums[mid])
                r = mid -1

        return minval