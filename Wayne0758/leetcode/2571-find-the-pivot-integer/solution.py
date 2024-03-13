class Solution:
    def pivotInteger(self, n: int) -> int:
        s=((1+n)*n)/4
        for i in range(1,n+1):
            if s<i:
                if s*2==i:
                    return i
                else:
                    return -1
            s-=i
