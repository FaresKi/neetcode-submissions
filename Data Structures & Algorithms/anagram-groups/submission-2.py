class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        anagrams = {}
        result = []

        for word in strs:
            sorted_word="".join(sorted(word))

            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        

        for groups in anagrams.values():
            result.append(groups)
        
        return result