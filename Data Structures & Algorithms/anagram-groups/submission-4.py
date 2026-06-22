from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        anagrams = defaultdict(list)

        for word in strs:
            sorted_word="".join(sorted(word))
            anagrams[sorted_word].append(word)
        
        return list(anagrams.values())