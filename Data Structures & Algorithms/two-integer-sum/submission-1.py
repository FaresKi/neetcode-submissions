class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       diff_map = {}

       for i, num in enumerate(nums):
            diff = target - num
            print(f"Diff: {diff} and diff_map {diff_map}")

            if diff in diff_map:
                return [diff_map[diff], i]
           
            diff_map[num] = i