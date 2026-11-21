class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()

        result = []
        interval = intervals[0]

        for i in range(1, len(intervals)):
            if interval:
                if interval[1] < intervals[i][0]:
                    result.append(interval)
                    interval = intervals[i]
                elif interval[0] > intervals[i][1]:
                    result.append(interval)
                else:
                    interval = [min(interval[0], intervals[i][0]), max(interval[1], intervals[i][1])]
    
        result.append(interval)
        return result
        