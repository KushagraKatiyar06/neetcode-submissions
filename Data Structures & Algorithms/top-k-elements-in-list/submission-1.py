class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        n = len(nums) + 1
        buckets = [[] for _ in range (n)]

        for num, count in frequency.items():
            buckets[count].append(num)

        result = []
        i = len(buckets) - 1
        while len(result) != k:
            if buckets[i]:
                for val in buckets[i]:
                    result.append(val)
                    if len(result) == k:
                        return result
            i -= 1
        return result
        