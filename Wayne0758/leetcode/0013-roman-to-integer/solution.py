class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        if s[0] =='M':
            res+=1000
        elif s[0] =='D':
            res+=500
        elif s[0] =='L':
            res+=50
        elif s[0] =='C':
            res+=100
        elif s[0] =='V':
            res+=5
        elif s[0] =='X':
            res+=10
        elif s[0] =='I':
            res += 1
        for i in range(1,len(s)):
            if s[i] =='M':
                res+=1000
                if s[i-1] =='C':
                    res += -200
            elif s[i] =='D':
                res+=500
                if s[i-1] =='C':
                    res += -200
            elif s[i] =='L':
                res+=50
                if s[i-1] =='X':
                    res += -20
            elif s[i] =='C':
                res+=100
                if s[i-1] =='X':
                    res += -20
            elif s[i] =='V':
                res+=5
                if s[i-1] =='I':
                    res += -2
            elif s[i] =='X':
                res+=10
                if s[i-1] =='I':
                    res += -2
            elif s[i] =='I':
                res += 1
            print(res)
        return res
