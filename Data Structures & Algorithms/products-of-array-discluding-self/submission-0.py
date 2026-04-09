class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #  in: 1, 2, 4, 6
        # out: 48, 24, 12, 8

        # for 1 it is 2 * 4 * 6 

        # 0, 1, 2, 8, 48
        # 48,24,6, 0 

        prefix = []
        sum = 1 
        for num in nums:
            prefix.append(sum)
            sum *= num
            
        print(prefix)
        # 1, 1, 2, 8

        suffix = []
        sum = 1
        for num in reversed(nums):
            suffix.append(sum)
            sum *= num
        
        suffix = suffix[::-1]
        print(suffix)

        products = []
        for i in range(len(nums)):
            product = prefix[i] * suffix[i]
            products.append(product)
        
        return products

