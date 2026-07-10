class Solution:
    encoding_char = "!"
    def encode(self, strs: List[str]) -> str:
       words = self.encoding_char.join(strs)
       return words

    def decode(self, s: str) -> List[str]:
        return s.split(self.encoding_char)

