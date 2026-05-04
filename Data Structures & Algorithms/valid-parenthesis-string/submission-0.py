class Solution:
    def checkValidString(self, s: str) -> bool:
        # minOpenPar treat every * as )
        # maxOpenPar treat every * as (
        minOpen = 0
        maxOpen = 0

        for char in s: 

            if char == "(":
                minOpen +=1
                maxOpen += 1
            elif char == ")":
                minOpen -= 1
                maxOpen -= 1
            else:
                minOpen -= 1
                maxOpen += 1
            
            if maxOpen < 0 :
                 return False

            if minOpen < 0:
                minOpen = 0     
        
        return True if minOpen == 0 else False
