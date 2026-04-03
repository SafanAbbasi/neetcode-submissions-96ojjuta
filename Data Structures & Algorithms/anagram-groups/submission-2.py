class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram = defaultdict(list)

        # # anagram = {} # sorted str -> str combinations. no default value 

        # for word in strs:
        #     sortedword = "".join(sorted(word)) 

        #     anagram[sortedword].append(word)

        #     # else:
        #     #     anagram[sortedword] = [word]

        # # Simpler — skip the loop entirely
        # return list(anagram.values())        
        
        # res = []
        # for key, words in anagram.items():
        #     res.append(words)
        
        # return res

        strdict = defaultdict(list)


        for word in strs:
            count = [0] * 26 # placeholder for each letter of the alphabet
            for char in word:
                
                count[ord(char) - ord('a')] += 1

            strdict[tuple(count)].append(word)

        return list(strdict.values())

 


