import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [ ((( (point[0] * point[0]) + (point[1] * point[1] )), point ) ) for point in points]
        heapq.heapify(distances)

        result = []
        for i in range(k):
            point = heapq.heappop(distances)[1]
            result.append(point)
        return result

        