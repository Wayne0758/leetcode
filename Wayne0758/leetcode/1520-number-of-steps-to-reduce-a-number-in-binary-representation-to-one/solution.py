class Solution:
    def numSteps(self, s: str) -> int:
        num=int(s,2)
        c=0
        while num != 1:
            if num%2==1:
                num+=1
                c+=1
            else:
                num=num//2
                c+=1
        return c
