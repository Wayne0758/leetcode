class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if (c == ']' and stack[-1] == '[') or (c == '}' and stack[-1] == '{') or (c == ')' and stack[-1] == '('):
                stack.pop(-1)
            else:
                stack.append(c)
        if not stack:
            return True
        return False
