class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        max_length = 0
        """
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
        """
        for num in nums:
            if num - 1 not in nums:
                current = num
                length = 1
                while current + 1 in nums:
                    current+=1
                    length+=1
                max_length = max(max_length, length)
        
        return max_length

            


        