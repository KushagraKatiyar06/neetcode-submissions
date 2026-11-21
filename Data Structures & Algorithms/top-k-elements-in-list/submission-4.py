class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        solution = []

        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1

        buckets = [None] * (len(nums) + 1)

        for i in range (len(buckets)):
            buckets[i] = []

        for num, freq in freq.items():
            buckets[freq].append(num)
        
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                for num in buckets[i]:
                    solution.append(num)
                    if len(solution) == k:
                        return solution

