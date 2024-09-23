class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c!=']':
                stack.append(c)
            else:
                tmp = ''
                while stack[-1]!='[':
                    tmp = stack.pop(-1)+tmp
                stack.pop(-1)
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop(-1)+k
                k = int(k)
                stack+=[tmp]*k
        return ''.join(stack)

