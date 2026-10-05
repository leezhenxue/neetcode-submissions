class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }

        for c in s:
            if c in mapping:
                element = stack.pop() if stack else ""
                if element != mapping[c]:
                    return False
            else:
                stack.append(c)

        return not stack