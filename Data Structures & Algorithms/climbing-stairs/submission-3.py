class Solution:
    def climbStairs(self, n: int) -> int:
        # given steps
        # two choices each time

        # n =1 
        # f(0) = 1 doesn't mean "1 way to take steps to reach 0". 
        # It means "there is 1 valid way to exist at the starting position" — which is just... standing there doing nothing.
        

        # one = number of ways to reach the step. 2 behind where you currently are
        # two = number of ways to reach the step. 1 behind where you currently are

        # all paths to 5 = all paths to 4 + all paths to 3
        # Because every path to 4 can extend to 5 (add one 1-step), and every path to 3 can extend to 5 (add one 2-step).

        # one = 1 # f(0)
        # two = 1 # f(1)

        # for i in range(2, n+1):
        #     one, two = two, two + one
        
        # return two

# ### using total var

#         one = 1 # f(0)
#         two = 1 # f(1)
#         total = 0
#         if n < 2:
#             return 1
#         for i in range(2,n+1):
            
#             total = (one + two)
#             one = two
#             two = total

#         return total

### recursive way 
        memo = {}
        
        def helper(n):
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        
        return helper(n)
