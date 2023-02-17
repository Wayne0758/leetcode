class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        n=set()
        for email in emails:
            a=email.split('@')
            for i in range(len(a[0])):
                if a[0][i]=='+':
                    a[0]=a[0][:i]
                    break
            a[0]=a[0].replace('.','')
            n.add(a[0]+'@'+a[1])
        return len(n)