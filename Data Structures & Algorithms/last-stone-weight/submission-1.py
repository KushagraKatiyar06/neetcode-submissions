import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [(-1 * stone) for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if x == y:
                continue
            elif x < y:
                y = y - x
                heapq.heappush(maxHeap, (-1 * y))

        if maxHeap:
            return (maxHeap[0] * -1)
        else:
            return 0           
        