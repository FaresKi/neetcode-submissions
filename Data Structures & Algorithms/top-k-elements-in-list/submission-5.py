class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = defaultdict(int)

        for num in nums:
            num_map[num]+=1
        
        return [
            keys
            for keys, values in num_map.items()
            if values >=k
        ]

    

    