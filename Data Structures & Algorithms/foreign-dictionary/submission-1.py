class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #  you can only learn letter ordering by comparing adjacent words in the list.

        adj = defaultdict(list) 
        in_degree = {char: 0 for word in words for char in word} # find every unique word and set to 0

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    # found an ordering rule: w1[j] comes before w2[j]
                    adj[w1[j]].append(w2[j])
                    in_degree[w2[j]] += 1
                    break

## Kahn's algo

        q = collections.deque()
        for char in in_degree:
            if in_degree[char] == 0:
                q.append(char)

        res = []
        while q:
            char = q.popleft()
            res.append(char)
            for nei in adj[char]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        if len(res) == len(in_degree):
            return "".join(res)
        return ""

