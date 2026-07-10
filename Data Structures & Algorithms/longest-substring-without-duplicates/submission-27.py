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
                print(f"Coming here with left value: {left} and char: {s[left]}")
                print(f"Coming here with right value: {right} and char: {s[right]}")
                longest_string+=s[right]
            else:
                print(f"Found duplicate: {s[right]} in current string: {longest_string}")
                left = left + 1
                longest_string = s[left]
                right = left
            size = max(size, len(longest_string))
            print(f"longest_string: {longest_string}")
        return size




        