class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        mn = 1
        mx = x
        while mn <= mx:
            mid = (mn+mx) // 2
            if mid == x/mid:
                return mid
            elif mid< x/mid:
                mn = mid+1
            elif mid> x/mid:
                mx = mid-1
        return mx
