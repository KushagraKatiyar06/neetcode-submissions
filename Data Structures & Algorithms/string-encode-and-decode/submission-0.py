class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded

    def decode(self, s: str) -> List[str]:
        
        solution = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            size = int(s[i:j])
            i = j + 1

            word = s[i:i + size]
            solution.append(word)
            i += size

        return solution
