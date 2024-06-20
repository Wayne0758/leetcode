class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = int(math.sqrt(c))
        for i in range(a,-1,-1):
            if i**2 == c:
                return True
            b2 = c-i**2
            if b2 == int(math.sqrt(b2))**2:
                return True
        return False
