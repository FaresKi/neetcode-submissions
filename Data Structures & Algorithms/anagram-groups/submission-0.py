class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==1:
            return [strs]

        result = []
        anagram_map = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            print(f"sorted word: {sorted_word}")
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]

        for key, value in anagram_map.items():
            result.append(value)
        return result

        