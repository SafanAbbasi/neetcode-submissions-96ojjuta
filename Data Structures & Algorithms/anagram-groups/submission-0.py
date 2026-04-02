class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {} # sorted str -> str combinations. no default value 

        for word in strs:
            sortedword = "".join(sorted(word)) 
            if sortedword in anagram:
                anagram[sortedword].append(word)
            else:
                anagram[sortedword] = [word]
        
        res = []
        for key, words in anagram.items():
            res.append(words)
        
        return res
 


