class Solution:
    def findMin(self, nums: List[int]) -> int:
        # let's try naive approach
        left, right = 0, len(nums) - 1
        index = 0
        while (left<=right):
            mid = (left+right)//2
            if nums[mid] < nums[index]:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return nums[index]
            
        
