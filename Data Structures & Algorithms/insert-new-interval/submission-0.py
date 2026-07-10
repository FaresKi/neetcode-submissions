class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)): # [new_a, new_b] , [current_a, current_b]
            current_a, current_b = intervals[i] 
            new_a, new_b = newInterval
            print(f"current_a: {current_a} - current_b: {current_b} - new_a: {new_a} - new_b: {new_b}")
            if new_b < current_a:
                result.append(newInterval)
                return result + intervals[i:]
            elif new_a > current_b:
                result.append(intervals[i])
            else:
                newInterval = [min(new_a, current_a), max(new_b, current_b)]
            
        result.append(newInterval)
        return result