from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if any consecutive chars contain all the letters in s1, then true
        # fixed window size of s1

        # s1dict = Counter(s1)
        # s2dict = defaultdict(int)
        # start = 0

        # for end in range(len(s2)):

        #     if (end - start + 1) > len(s1):
        #         s2dict[s2[start]] -= 1
        #         if s2dict[s2[start]] == 0:
        #             del s2dict[s2[start]] # remove the key entry completely

        #         start += 1

            
        #     s2dict[s2[end]] += 1

        #     if s1dict == s2dict:
        #         return True 


        # return False
        

        # could use a array of size 26
        char1_arr = [0] * 26
        char2_arr = [0] * 26

        start = 0

        for char in s1:
            char1_arr[ord(char) - ord('a')] += 1

        print(char1_arr)
        for end in range(len(s2)):

            if (end - start + 1) > len(s1):
                char2_arr[ord(s2[start]) - ord('a')] -= 1

                start += 1

            
            char2_arr[ord(s2[end]) - ord('a')] += 1

            print(char2_arr)
            if char1_arr == char2_arr:
                return True 


        return False
        