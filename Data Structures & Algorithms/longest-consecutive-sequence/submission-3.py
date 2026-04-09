class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # I can't sort becuase that would be O(n*logn)


        # can store each unique number in a set
        numset = set(nums)
        # for num in nums:
        #     if num not in numset:
        #         numset.add(num)

        longest = 0
        for num in nums:
            if num-1 not in numset:
                # it must be a valid starting value if num -1 not in the set
                count = 0
                current = num

                while current in numset: 
                    count += 1
                    current += 1
                
                longest = max(longest, count) 

        return longest