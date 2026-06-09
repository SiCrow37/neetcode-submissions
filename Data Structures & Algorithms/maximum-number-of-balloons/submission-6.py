class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {}
        m = -1

        for t in text:
            if t in "balloon":
                if t not in d:
                    d[t] = 1
                else: 
                    d[t] += 1

        n = 0
        while d:
            for t in "balloon":
                if t not in d:
                    return n
                if t == 'b':
                    d['b'] -= 1
                if t == 'a':
                    d['a'] -= 1
                if t == 'l':
                    d['l'] -= 1
                if t == 'o':
                    d['o'] -= 1
                if t == 'n':
                    d['n'] -= 1
                if d[t] < 0:
                    return n
            n += 1
        return n
