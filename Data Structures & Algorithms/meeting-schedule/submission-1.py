"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)

        if not intervals or len(intervals) == 1:
            return True

        for i in range(1, len(intervals)):
            compare1 = intervals[i - 1]
            compare2 = intervals[i]

            if compare1.end > compare2.start:
                return False

        return True
