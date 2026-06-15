class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}
        c = 0
        wds = len(words)

        for w in words:
            for ch in w:
                if ch not in d:
                    d[ch] = 1
                else:
                    d[ch] += 1
        
        for k in d:
            if d[k] % wds != 0 or d[k] < wds:
                return False
        
        return True
