class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        elif len(intervals) == 1:
            return 0

        intervals.sort()
        
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            compare2 = intervals[i]
            compare1 = res[-1]

            if compare1[1] > compare2[0]: 
                if compare2[1] < compare1[1]:
                    res[-1] = compare2
               
            else:
                
                res.append(compare2)

        return len(intervals) - len(res)


        