class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums).most_common(k)

        return list(map(lambda c: c[0], counter))