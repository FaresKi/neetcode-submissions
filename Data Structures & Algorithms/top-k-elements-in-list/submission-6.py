class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = defaultdict(int)

        for num in nums:
            num_map[num]+=1
        
        sorted_items = sorted(
            num_map.items(),
            key=lambda e: e[1],
            reverse=True
        )

        return list(map(
            lambda e: e[0],
            sorted_items
        ))[:k]

    

    