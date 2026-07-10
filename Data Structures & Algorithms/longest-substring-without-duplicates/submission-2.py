class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dynamic sliding window because there's no fixed size in the instructions
        if not s:
            return 0
        longest_string = s[0]
        size = 1
        right = 1
        for c in range(right, len(s)):
            if s[c] not in longest_string:
                longest_string+=s[c]
            else:
                size = max(size, len(longest_string))
                longest_string = s[c]

        return size




        