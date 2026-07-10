class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr:
            return True
        return len(word[1:-1]) == int(abbr[1:-1].strip())