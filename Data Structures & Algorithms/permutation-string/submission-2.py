from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if any consecutive chars contain all the letters in s1, then true
        # fixed window size of s1

        s1dict = Counter(s1)

        s2dict = defaultdict(int)

        start = 0

        for end in range(len(s2)):

            if (end - start + 1) > len(s1):
                s2dict[s2[start]] -= 1
                if s2dict[s2[start]] == 0:
                    del s2dict[s2[start]] # remove the key entry completely

                start += 1

            
            s2dict[s2[end]] += 1
            print(s2dict)
            
            if s1dict == s2dict:
                return True 


        return False
        
