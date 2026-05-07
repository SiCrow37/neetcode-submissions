class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        r = [-1] * len(temperatures)
        i = 0

        for t in temperatures:
            if len(s) == 0:
                s.append((t, i))
            elif t > s[-1][0]:
                while s and t > s[-1][0]:
                    r[s[-1][1]] = i - s[-1][1]
                    s.pop()
                s.append((t, i))
            elif s and t <= s[-1][0]:
                s.append((t, i))
            
            i += 1
        i = 0

        while i < len(r):
            if r[i] == -1:
                r[i] = 0
            i += 1
        
        return r

            
                
            