class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # I can't sort becuase that would be O(n*logn)


        # can store each unique number in a set
        numset = set()
        for num in nums:
            if num not in numset:
                numset.add(num)
        longest = 0
        for num in nums:
            if num-1 not in numset:
                # it must be a valid starting value if num -1 not in the set
                long = 0
                nextval = num

                while nextval in numset: 
                    long += 1
                    nextval += 1
                
                longest = max(longest, long) 

        return longest