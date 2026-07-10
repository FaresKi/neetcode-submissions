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
            if not stack:
                return False
            
            stack.pop()
        
        return not stack
            