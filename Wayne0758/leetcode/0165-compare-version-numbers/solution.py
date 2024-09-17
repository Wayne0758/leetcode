class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        n = max(len(version1),len(version2))
        version1 += [0] * (n-len(version1))
        version2 += [0] * (n-len(version2))
        for i in range(n):
            if int(version1[i])>int(version2[i]):
                return 1
            elif int(version1[i])<int(version2[i]):
                return -1
        return 0
