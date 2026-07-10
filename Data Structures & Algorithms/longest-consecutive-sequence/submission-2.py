class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        consecutive_nums = [1]
        sorted_nums = sorted(nums)
        i=0
        print(sorted_nums)
        while (i<len(nums)-1):
            if sorted_nums[i+1]==sorted_nums[i]+1:
                print(f"Consecutive: {consecutive} i+1: {sorted_nums[i+1]} - i: {sorted_nums[i]}")
                consecutive+=1
            elif sorted_nums[i+1]==sorted_nums[i]:
                print(f"Same: i+1: {sorted_nums[i+1]} - i: {sorted_nums[i]}")
                pass
            else:
                print(f"Not the same: i+1: {sorted_nums[i+1]} - i: {sorted_nums[i]}")
                consecutive=1
            consecutive_nums.append(consecutive)
            i+=1
        
        return max(consecutive_nums)

        