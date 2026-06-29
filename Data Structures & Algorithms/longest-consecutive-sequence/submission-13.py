class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(f"sorted nums: {nums}")
        consecutive_nums = {nums[0]}
        max_size = 0
        i = 1
        while i < len(nums):
            if nums[i] in consecutive_nums:
                i+=1
            else:
                if nums[i] == nums[i-1]+1:
                    consecutive_nums.add(nums[i])
                    i+=1
                else:
                    max_size = max(max_size, len(consecutive_nums))
                    consecutive_nums = {nums[i]}
                    i+=1
                
        max_size = max(max_size, len(consecutive_nums))
        return max_size
            


        