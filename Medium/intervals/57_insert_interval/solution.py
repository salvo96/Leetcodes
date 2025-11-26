class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        output_lst = [intervals[0]]
        for interval in intervals[1:]:
            last_interval = output_lst[-1]

            if last_interval[1] >= interval[0]:
                output_lst[-1] = [last_interval[0], max(interval[1], last_interval[1])]
            else:
                output_lst.append(interval)
        return output_lst
