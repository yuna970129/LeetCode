class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                if stack:
                    top = stack.pop()
                    if mapping[char] != top:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        print(stack)
            
        return not stack
