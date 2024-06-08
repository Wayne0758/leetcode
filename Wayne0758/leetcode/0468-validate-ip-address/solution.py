class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.checkIPv4(queryIP):
            return "IPv4"
        if self.checkIPv6(queryIP):
            return "IPv6"
        return "Neither"
    def checkIPv4(self, queryIP: str) -> bool:
        queryIP+='.'
        valid = ['0','1','2','3','4','5','6','7','8','9']
        a=''
        b=0
        for c in queryIP:
            if c =='.':
                if 1<= len(a) <=3:
                    if a[0] == '0' and len(a)>1:
                        return False
                    if 0<=int(a)<= 255:
                        b+=1
                else:
                    return False
                a=''
                continue
            if c not in valid:
                return False
            a+=c
        if b!=4:
            return False
        return True
    def checkIPv6(self, queryIP: str) -> bool:
        queryIP+=':'
        valid = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','A','B','C','D','E','F']
        a=''
        b=0
        for c in queryIP:
            if c ==':':
                if 1<= len(a) <=4:
                    b+=1
                    print(a)
                else:
                    return False
                a=''
                continue
            if c not in valid:
                return False
            a+=c
        if b!=8:
            return False
        return True
