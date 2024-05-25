class Solution:
    def __init__(self):
        self.res = []

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.dfs(s, wordDict, [], 0)
        return self.res

    def dfs(self, s: str, wordDict: List[str], savewords: List[str], start: int):
        if len(s) == 0:
            self.res += [' '.join(savewords)]
            return
        for word in wordDict:
            if word == s[:len(word)]:
                self.dfs(s[len(word):], wordDict, savewords+[word], start+len(word))
