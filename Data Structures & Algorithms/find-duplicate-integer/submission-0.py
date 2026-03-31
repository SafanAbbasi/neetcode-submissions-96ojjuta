class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        uniqueset = set()

        for num in nums:

            if num in uniqueset:
                return num
            else:
                uniqueset.add(num)
        