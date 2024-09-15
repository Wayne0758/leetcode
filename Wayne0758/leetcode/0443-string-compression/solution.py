class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        chars.append(0)
        res = []
        tmp=1
        for i in range(n):
            if chars[i]==chars[i+1]:
                tmp+=1
            else:
                if tmp==1:
                    res+=chars[i]
                    tmp=1
                else:
                    res+=chars[i]+str(tmp)
                    tmp=1
        res = list(res)
        for i in range(len(res)):
            chars[i] = res[i]
        return len(res)

