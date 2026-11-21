class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {} # contains signature, and list of values inside it

        for string in strs:
            signature = [0] * 26
            for char in string:
                signature[ord(char) - ord('a')] += 1
            key = tuple(signature)
            
            if key in groups:
                groups[key].append(string)
            else:
                groups[key] = []
                groups[key].append(string)

            
        return list(groups.values())
            
        