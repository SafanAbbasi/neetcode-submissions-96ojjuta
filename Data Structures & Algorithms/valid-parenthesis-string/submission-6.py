class Solution:
    def checkValidString(self, s: str) -> bool:
        parstack = []
        wildstack = []

        for i, char in enumerate(s):

            if char == ")":
                if parstack:
                    parstack.pop()
                elif wildstack:
                    wildstack.pop()
                else: 
                    return False 
            elif char == "*":
                wildstack.append(i)
            else:
                parstack.append(i)
       
        while parstack and wildstack:
            if wildstack[-1] > parstack[-1]:
                # valid match, pop both
                wildstack.pop()
                parstack.pop()
            else:
                # * comes before (, can't use it as )
                return False
        
        return len(parstack) == 0
       
       
       
       
       
       
        # minOpenPar treat every * as )
        # maxOpenPar treat every * as (
        # minOpen = 0
        # maxOpen = 0

        # for char in s: 

        #     if char == "(":
        #         minOpen +=1
        #         maxOpen += 1
        #     elif char == ")":
        #         minOpen -= 1
        #         maxOpen -= 1
        #     else:
        #         minOpen -= 1
        #         maxOpen += 1
            
        #     if maxOpen < 0 :
        #          return False

        #     if minOpen < 0:
        #         minOpen = 0     
        
        # return True if minOpen == 0 else False
