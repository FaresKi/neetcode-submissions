class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dynamic sliding window because there's no fixed size in the instructions
        if not s:
            return 0
        left = 0
        longest_string = s[left]
        size = 1
        right = 1
        for right in range(left, len(s)):
            print(f"left: {left} - right: {right}")
            print(f"longest_string: {longest_string}")
            if s[right] not in longest_string:
                longest_string+=s[right]
            else:
                longest_string = s[right]
                left = left + 1
            size = max(size, len(longest_string))
        return size




        