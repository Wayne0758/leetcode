class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=0
        for num in nums:
            x = x ^ num
        bitx=str(bin(x)).zfill(35)
        for i in range(len(bitx)):
            if bitx[i] == '1':
                tmp=0
                for num in nums:
                    if str(bin(num)).zfill(35)[i] == '1':
                        tmp = tmp^num
                return [tmp, tmp^x]
