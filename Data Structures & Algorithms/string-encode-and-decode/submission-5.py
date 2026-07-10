class Solution:
    encoding_char = "!"
    def encode(self, strs: List[str]) -> str:
       if not strs:
        return ""
       words = self.encoding_char.join(strs)
       return words

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        return s.split(self.encoding_char)

