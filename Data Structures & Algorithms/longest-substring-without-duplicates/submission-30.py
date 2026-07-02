class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dynamic sliding window because there's no fixed size in the instructions
        if not s:
            return 0
        left = 0
        longest_string = ""
        size = 1
        for right in range(left, len(s)):
            print(f"left: {left} - right: {right}")
            if s[right] not in longest_string:
                longest_string+=s[right]
            else:
                while s[right] in longest_string:
                    longest_string = longest_string[1:]
                longest_string += s[right]
            size = max(size, len(longest_string))
        return size