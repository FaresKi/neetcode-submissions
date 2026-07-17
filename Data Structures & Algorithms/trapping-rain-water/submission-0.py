class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        height_left, height_right = height[left], height[right]
        res = 0
        while left < right:
            if height_left < height_right:
                left+=1
                height_left = max(height_left, height[left])
                res+= height_left - height[left]
            else:
                right-=1
                height_right = max(height_right, height[right])
                res+= height_right - height[right]
        
        return res

