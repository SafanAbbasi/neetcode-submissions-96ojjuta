class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # so we know that we have to exhuast all counts of a character to move on else the substring gets bigger

        freq = collections.defaultdict(int)
        for char in s:
            freq[char] +=1

        res = [] # store answers
        sublength = 0
        charset = set()
        for i, char in enumerate(s):

            sublength += 1
            freq[char] -= 1
            charset.add(char)

            if all(freq[c] == 0 for c in charset):
                res.append(sublength)
                sublength = 0
                charset = set()
            
        return res