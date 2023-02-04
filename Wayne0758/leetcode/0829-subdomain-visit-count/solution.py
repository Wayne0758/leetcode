class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        a=[]
        d=collections.defaultdict(int)
        for domain in cpdomains:
            a=domain.split(' ')
            times=int(a[0])
            subdomains=a[1]
            d[subdomains] += times
            while '.' in subdomains:
                subdomains=subdomains[subdomains.index('.')+1:]
                d[subdomains] += times
        return [str(value)+' '+key for key,value in d.items()]
