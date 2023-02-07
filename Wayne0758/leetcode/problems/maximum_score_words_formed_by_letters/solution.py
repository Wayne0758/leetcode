class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        cnt=[0 for _ in range(26)]
        for l in letters:
            cnt[ord(l)-97]+=1
        return self.dfs(words,cnt,score,0)
    def dfs(self,words,cnt,score,idx):
        res=0
        for i in range(idx,len(words)):
            s=0
            flag=1
            for c in words[i]:
                cnt[ord(c)-97]-=1
                if cnt[ord(c)-97]<0:
                    flag=0
                s+=score[ord(c)-97]
            if flag==1:
                s+=self.dfs(words,cnt,score,i+1)
                res=max(res,s)
            for c in words[i]:
                cnt[ord(c)-97]+=1
        return res