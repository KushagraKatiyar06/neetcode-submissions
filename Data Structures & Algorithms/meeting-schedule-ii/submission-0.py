"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = [interval.start for interval in intervals]
        endTimes = [interval.end for interval in intervals]
        startTimes.sort()
        endTimes.sort()

        count = 0
        most = 0
        s, e = 0, 0
        while s < len(intervals):
            if startTimes[s] < endTimes[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            most = max(most, count)
        return most