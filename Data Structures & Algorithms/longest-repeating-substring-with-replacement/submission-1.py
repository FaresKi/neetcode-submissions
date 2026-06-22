class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_count_values = max(count.values())
            window_length = r - l + 1

            while (window_length - max_count_values) > k:
                print(f"window_length: {window_length}")
                print(f"max_count_values: {max_count_values}")
                count[s[l]]-=1
                l+=1
                window_length = r - l + 1
                max_count_values = max(count.values())
            
            res = max(res, window_length)
        
        return res