class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        t = 0
        k = {}



        for i in range(len(keyboard)):
            k[keyboard[i]] = i

        for i in range(len(word)):
            if i == 0: 
                t = k[word[i]]
            else:
                t += abs(k[word[i]] - k[word[i-1]])

        return t
