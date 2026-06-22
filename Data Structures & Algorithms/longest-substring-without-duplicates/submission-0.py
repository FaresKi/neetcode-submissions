class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_set = set()
        max_length = 0

        for r in range(len(s)):
            print(f"char_set: {char_set} - s[l]: {s[l]} - s[r]: {s[r]}")
            while s[r] in char_set:
                char_set.remove(s[l])
                print(f"char_set in while loop: {char_set} - s[l]: {s[l]} - s[r]: {s[r]}")
                l+=1
            char_set.add(s[r])
            max_length = max(max_length, r+1-l)
        
        return max_length



        