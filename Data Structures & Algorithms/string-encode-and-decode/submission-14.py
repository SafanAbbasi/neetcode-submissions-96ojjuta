class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "/0"

        encode = []
        for word in strs:
            encoding = ""
            for char in word:
                if char == "/":
                    encoding += "//"
                elif char == ",":
                    encoding += "/,"
                else:
                    encoding += char
            encode.append(encoding)

        return ",".join(encode)

    def decode(self, s: str) -> List[str]:
        if s == "/0":
            return []

        decoded = []
        word = ""
        idx = 0
        while idx < len(s):
            char = s[idx]
            if char == "/" and idx+1 < len(s) and s[idx+1] == "/":
                word += "/"
                idx += 2
            elif char == "/" and idx+1 < len(s) and s[idx+1] == ",":
                word += ","
                idx += 2
            elif char == ",":
                decoded.append(word)
                word = ""
                idx += 1
            else:
                word += char
                idx += 1

        decoded.append(word)
        return decoded