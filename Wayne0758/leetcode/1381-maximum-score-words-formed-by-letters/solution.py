class Solution:
    def __init__(self):
        self.hashmap = collections.defaultdict(int)
    
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        for letter in letters:
            self.hashmap[letter] += 1
        wordscores = self.getscore(words, score)
        return self.dfs(wordscores, dict(self.hashmap), 0, 0)

    def dfs(self, wordscores: List[tuple], hashmaptmp, start: int, tmpscore: int) -> int:
        maxscore = tmpscore
        for i in range(start, len(wordscores)):
            word, wordscore, letter_count = wordscores[i]
            if self.can_form_word(letter_count, hashmaptmp):
                self.update_hashmap(letter_count, hashmaptmp, decrement=True)
                maxscore = max(maxscore, self.dfs(wordscores, hashmaptmp, i + 1, tmpscore + wordscore))
                self.update_hashmap(letter_count, hashmaptmp, decrement=False)
        return maxscore

    def getscore(self, words: List[str], score: List[int]) -> List[tuple]:
        wordscores = []
        for word in words:
            wordscore = 0
            letter_count = collections.defaultdict(int)
            for c in word:
                wordscore += score[ord(c) - ord('a')]
                letter_count[c] += 1
            wordscores.append((word, wordscore, letter_count))
        return wordscores

    def can_form_word(self, letter_count, hashmaptmp):
        for c in letter_count:
            if letter_count[c] > hashmaptmp.get(c, 0):
                return False
        return True

    def update_hashmap(self, letter_count, hashmaptmp, decrement=True):
        for c in letter_count:
            if decrement:
                hashmaptmp[c] -= letter_count[c]
            else:
                hashmaptmp[c] += letter_count[c]
