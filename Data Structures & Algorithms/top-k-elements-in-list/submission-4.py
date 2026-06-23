class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_nums = {}
        for num in nums:
            if num in frequent_nums:
                frequent_nums[num]+=1
            else:
                frequent_nums[num]=1
        
        frequent_nums_sorted = sorted(frequent_nums, key=lambda x: frequent_nums[x], reverse=True)[:k]
        return frequent_nums_sorted
        