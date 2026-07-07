class Solution:
    def findMin(self, nums: List[int]) -> int:
        # let's try naive approach
        l, r = 0, len(nums) - 1
        index = -1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] < nums[index]:
                index = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return nums[index]
            
        
