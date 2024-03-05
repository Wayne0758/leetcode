class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s)==0:
            return 0
        while s[0] == s[-1] and len(s) != 0:
            a=s[0]
            if len(s)==1:
                return 1
            while s[0]==a:
                s=s[1:]
                if len(s)==0:
                    return 0
            while s[-1]==a:
                s=s[:-1]
                if len(s)==0:
                    return 0
        return len(s)
