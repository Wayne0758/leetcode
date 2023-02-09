class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        self.m=len(mat)
        self.n=len(mat[0])
        ans=self.m*self.n+1
        for i in range(2**self.m):
            s=[[0 for _ in range(self.n)] for _ in range(self.m)]
            a=bin(i)[2:]
            cnt=0
            a=a.zfill(self.n)
            for j in range(self.n):
                if a[j]=='1':
                    cnt+=1
                    s=self.flip(s,0,j)
            for j in range(1,self.m):
                for k in range(self.n):
                    if s[j-1][k]^mat[j-1][k]:
                        cnt+=1
                        s=self.flip(s,j,k)
            flag=1
            for j in range(self.n):
                if s[self.m-1][j]^mat[self.m-1][j]:
                    flag=0
                    break
            if flag:
                ans=min(ans,cnt)
        if ans==self.m*self.n+1:
            return -1
        return ans
    def flip(self,s,x,y):
        dirs=[0,1,0,-1,0,0]
        for i in range(5):
            tx=x + dirs[i]
            ty=y + dirs[i+1]
            if 0<=tx<self.m and 0<=ty<self.n :
                s[tx][ty]^=1
        return s