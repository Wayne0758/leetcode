class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        b=[]
        d=[]
        for path in paths:
            if path[1] not in b:
                d.append(path[1])
            else:
                b.remove(path[1])
            if path[0] not in d:
                b.append(path[0])
            else:
                d.remove(path[0])
        return d[0]
