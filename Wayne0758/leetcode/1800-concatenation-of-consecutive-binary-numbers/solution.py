class Solution:
    def concatenatedBinary(self, n: int) -> int:
        kmod = 10**9+7
        ans = 0
        length = 0
        for i in range(n):
            if (i & (i+1)) == 0:
                length += 1
            ans = ((ans << length) % kmod + i+1) % kmod
        return ans
