class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        
        for word in strs:
            encoded.append(str(len(word)))
            encoded.append('#')
            encoded.append(word)

        return ''.join(encoded)


    def decode(self, s: str) -> List[str]:
        solution = []
        i = 0
        j = 0

        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            i = j + 1
            j = j + length + 1

            currentWord = s[i:j]
            solution.append(currentWord)

            i = i + length
        
        return solution



            
