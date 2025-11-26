class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))

        count_removal = 0
        last_interval = intervals[0]
        for interval in intervals[1:]:
            if last_interval[1] > interval[0]:
                count_removal += 1
                if last_interval[1] > interval[1]:
                    last_interval = interval
            else:
                last_interval = interval
        return count_removal
