class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a=s.count('1')
        b=s.count('0')
        ans='1'
        for i in range(b):
            ans = '0' + ans
        for j in range(a-1):
            ans = '1' + ans
        return ans