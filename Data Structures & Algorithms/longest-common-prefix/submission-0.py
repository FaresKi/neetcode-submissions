class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word, *rest = strs

        while first_word is not None:
            if not all(first_word in word for word in rest):
                first_word = first_word[:-1]
            else:
                break
        
        return first_word
        