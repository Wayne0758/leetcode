class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        l=0.0
        r=1.0
        while l<r:
            m=(l+r)/2
            max_f = 0.0
            total = 0
            j=1
            p=0
            q=0
            for i in range(n-1):
                while j < n and arr[i] > m*arr[j]:
                    j+=1
                if j == n:
                    break
                total += n-j
                f = arr[i] / arr[j]
                if f > max_f:
                    p, q, max_f = i, j, f
            if total == k:
                return [arr[p], arr[q]]
            elif total>k:
                r=m
            else:
                l=m
        return []
