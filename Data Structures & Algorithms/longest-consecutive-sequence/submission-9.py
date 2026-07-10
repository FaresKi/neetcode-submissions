class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        consecutive_nums = {nums[0]}
        max_size = 0
        i = 1
        while i < len(nums):
            if nums[i] in consecutive_nums:
                i+=1
            else:
                print(f"consecutive_nums: {consecutive_nums} - i: {i} - num: {nums[i]}")
                if nums[i] == nums[i-1]+1:
                    print(f"num: {nums[i]}")
                    consecutive_nums.add(nums[i])
                    i+=1
                else:
                    max_size = max(max_size, len(consecutive_nums))
                    consecutive_nums = set()
                    i+=1
                
        max_size = max(max_size, len(consecutive_nums))
        return max_size
            


        