class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "}" : "{",
            ")" : "(",
            "]" : "[",
        }

        stack = []

        for char in s:
            if char not in map:
                stack.append(char)
                continue
            else:
                stack.pop()
        
        return not stack
            