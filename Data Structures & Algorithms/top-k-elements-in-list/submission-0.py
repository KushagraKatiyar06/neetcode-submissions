from collections import OrderedDict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = OrderedDict()

        for num in nums:
            frequency[num] = frequency.get(num,0) + 1

        sorted_keys = sorted(frequency.items(), key = lambda x: x[1], reverse = True)
        count = 0  
        solution = []

        for key, value in (sorted_keys):
            if count < k:
                solution.append(key)
                count += 1
            else:
                break
        
        return solution



        