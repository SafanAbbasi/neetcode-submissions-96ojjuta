class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        # anagram = {} # sorted str -> str combinations. no default value 

        for word in strs:
            sortedword = "".join(sorted(word)) 

            anagram[sortedword].append(word)
            
            # else:
            #     anagram[sortedword] = [word]

        # Simpler — skip the loop entirely
        return list(anagram.values())        
        
        # res = []
        # for key, words in anagram.items():
        #     res.append(words)
        
        # return res
 


