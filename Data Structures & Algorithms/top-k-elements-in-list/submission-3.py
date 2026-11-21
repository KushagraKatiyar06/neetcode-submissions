class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequent = {}

        for num in nums:
            frequent[num] = frequent.get(num, 0) + 1

        n = len(nums) + 1

        buckets = [[] for _ in range(n)]

        for num, count in frequent.items():
            buckets[count].append(num)

        result = []

        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i]:
                for num in buckets[i]:
                    result.append(num)
                    if len(result) == k:
                        return result


        return result


        