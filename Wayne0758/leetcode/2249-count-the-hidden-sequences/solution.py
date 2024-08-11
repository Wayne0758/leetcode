class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        for i in range(1,len(differences)):
            differences[i] += differences[i-1]
        differences.append(0)
        mn = min(differences)
        mx = max(differences)
        if (upper-lower) - (mx-mn)+1<0:
            return 0
        return (upper-lower) - (mx-mn)+1
