class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        left = 0
        count_window, count_t = {}, {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
        
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float('inf')

        for right in range(len(s)):
            c = s[right]
            count_window[c] = 1 + count_window.get(c, 0)

            if c in count_t and count_window[c] == count_t[c]:
                have+=1
            
            while have==need:
                if (right - left + 1) < res_len: # we want to minimize length
                    res = [left, right]
                    res_len = (right - left + 1)
                
                # pop the left from the window
                count_window[s[left]]-=1
                if s[left] in count_t and count_window[s[left]] < count_t[s[left]]:
                    have-=1 # remove eligible character when moving left pointer
                
                left+=1
        
        left, right = res
        return s[left: right+1] if res_len != float('inf') else ""





        
        