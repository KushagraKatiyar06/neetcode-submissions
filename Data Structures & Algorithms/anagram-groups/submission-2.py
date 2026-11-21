class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for word in strs:
            signature = [0] * 26

            for char in word:
                signature[ord(char) - ord('a')] += 1

            key = tuple(signature)
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = []
                anagrams[key].append(word)

        return list(anagrams.values())
        