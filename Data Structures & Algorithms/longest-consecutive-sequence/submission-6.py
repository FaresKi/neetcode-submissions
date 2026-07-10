class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        consecutive_nums = set()

        i = 1
        max_size = 0
        
        while i < len(nums):
            print(f"i: {i} - nums: {nums[i]}")
            if nums[i] == nums[i-1] + 1:
                print(f"nums: {nums[i]}")
                consecutive_nums.add(nums[i-1])
                consecutive_nums.add(nums[i])
                max_size = max(max_size, len(consecutive_nums))
                i+=1
            elif nums[i-1] == nums[i]:
                i+=1
            else:
                print(f"i-1: {nums[i-1]} - i: {nums[i]} ")
                max_size = max(max_size, len(consecutive_nums))
                consecutive_nums = set()
                i+=1
        
        return max_size
            


        