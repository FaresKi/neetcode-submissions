class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_map = defaultdict()

        for num in nums:
            if num_map.get(num, None) is not None:
                num_map[num] += 1
            else:
                num_map[num] = 1

        return list(filter(lambda a: num_map[a]>=k, num_map.keys()))
