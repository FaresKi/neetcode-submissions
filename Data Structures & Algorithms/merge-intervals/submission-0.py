class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # use different sorting mechanism after
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            current_a, current_b = intervals[i]
            last_a, last_b = result[-1]
            if current_a <= last_b:
                result[-1][1] = max(current_b, last_b)
            else:
                result.append(intervals[i])
        
        return result
