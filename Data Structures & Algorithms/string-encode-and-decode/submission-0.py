class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word))+"!"+word
        print(f"encoded_str: {encoded_str}")
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j=i
            while s[j]!="!":
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        
        return result


