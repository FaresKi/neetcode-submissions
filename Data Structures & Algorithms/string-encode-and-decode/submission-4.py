class Solution:
    encoding_char = "!"
    def encode(self, strs: List[str]) -> str:
       words = self.encoding_char.join(strs)
       print(words)
       return words

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        return s.split(self.encoding_char)

