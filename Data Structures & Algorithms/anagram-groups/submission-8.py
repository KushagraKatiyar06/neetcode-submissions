class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     
        solution = []
        anagrams = {}

        for str in strs:
            currentKey = [0] * 26

            for char in str:
                currentKey[ord(char) - ord('a')] += 1
            key = tuple(currentKey)

            if key in anagrams:
                anagrams[key].append(str)
            else:
                anagrams[key] = []
                anagrams[key].append(str)
            
        for key, value in anagrams.items():
            solution.append(value)

        return solution