class Solution:
    def merge(self, intervals):
        result = []
        if not intervals:
            return result
        intervals.sort(key=lambda x: x.start)
        result.append(intervals[0])
        for i in range(intervals[1:]):
            last_interval = result[-1]
            if last_interval.end >= interval.start:
                last_interval.end = max(last_interval.end, interval.end)
            else:
                result.append(interval)
        return result
