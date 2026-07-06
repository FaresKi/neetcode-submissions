from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        k = len(s1)
        s1_freq = Counter(s1)
        window_freq = Counter(s2[:k])
        
        if window_freq == s1_freq:
            return True
        
        for i in range(k, len(s2)):
            # Add new char
            window_freq[s2[i]] += 1
            # Remove old char
            window_freq[s2[i-k]] -= 1
            if window_freq[s2[i-k]] == 0:
                del window_freq[s2[i-k]]
            # Check match
            if window_freq == s1_freq:
                return True
        
        return False