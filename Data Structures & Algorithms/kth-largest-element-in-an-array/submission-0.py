import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [(-1 * num) for num in nums]
        heapq.heapify(maxHeap)

        result = -1
        for i in range(k):
            result = heapq.heappop(maxHeap)

        return (result * -1)


        