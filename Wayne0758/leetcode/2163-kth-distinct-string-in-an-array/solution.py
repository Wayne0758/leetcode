class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        appeared = set()
        unique = []
        for c in arr:
            if c in appeared:
                if c in unique:
                    unique.remove(c)
            else:
                appeared.add(c)
                unique.append(c)
        if k>len(unique):
            return ''
        return unique[k-1]
