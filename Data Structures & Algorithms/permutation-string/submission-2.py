from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        k = len(s1)
        window_freq = Counter(s2[:k])
        s1_freq = Counter(s1)

        if window_freq == s1_freq:
            return True
        
        for i in range(k, len(s2)):
            left = i - k
            window_freq[s2[i]]+=1
            window_freq[s2[left]]-=1

            if window_freq[s2[left]] == 0:
                window_freq.pop(s2[left])
            if window_freq == s1_freq:
                return True
        
        return False

