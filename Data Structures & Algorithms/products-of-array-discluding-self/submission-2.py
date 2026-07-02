import functools
import copy

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i, num in enumerate(nums):
            filtered_list = copy.deepcopy(nums)
            filtered_list.pop(i)
            product = functools.reduce(lambda a, b: a*b, filtered_list)
            result.append(product)

        return result
        