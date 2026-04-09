class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted array
        # example [ 1, 4, 7, 10, 12] # target = 14 answer is [2,4]
        # shift pointer based off being lower or higher than target

        left, right = 0 , len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right] 

            if total < target: # too small so left needs to increse
                left += 1
            
            elif total > target: # too big
                right -= 1
            
            else: # total == target
                return [left+1, right+1]
        