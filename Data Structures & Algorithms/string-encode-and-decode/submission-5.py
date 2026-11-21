class Solution:

    def encode(self, strs: List[str]) -> str:
        # cat, bat, eat -> 3#cat3#bat3#eat -> cat, bat, eat
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#'
            encoded += s

        return encoded

    def decode(self, s: str) -> List[str]:
        solution = []

        # 3#cat3#bat3#eat10#abcdefghij
        i = 0
        j = 0
        
        while i < len(s):

            count = ""
            while s[i] != '#':
                count += s[i]
                i += 1
            count = int(count)

            i = i + 1
            j = i + count

            currentString = s[i : j]
            solution.append(currentString)

            i = j
            
        return solution

