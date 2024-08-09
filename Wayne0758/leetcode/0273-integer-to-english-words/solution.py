class Solution:
    def numberToWords(self, num: int) -> str:
        s = []
        a = ['','Thousand','Million','Billion']
        digit = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        aboveten = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        tendigit = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        c = 0
        if num == 0:
            return 'Zero'
        while num:
            stmp = []
            tmp = num % 1000
            num = (num-tmp) // 1000
            if tmp == 0:
                c+=1
                continue
            tmp = str(tmp).zfill(3)
            hun = int(tmp[0])
            if hun > 0:
                stmp += [digit[hun],'Hundred']
            ten = int(tmp[1])
            dig = int(tmp[2])
            if ten == 1 and aboveten[dig]!='':
                stmp += [aboveten[dig]]
            else:
                if tendigit[ten] !='':
                    stmp += [tendigit[ten]]
                if digit[dig] !='':
                    stmp += [digit[dig]]
            if c != 0:
                s = stmp+[a[c]]+s
            else:
                s = stmp+s
            c+=1
        return ' '.join(s)[:]
