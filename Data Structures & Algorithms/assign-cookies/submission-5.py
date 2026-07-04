class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        d = defaultdict(int)
        c = 0

        for j in s:
            d[j] += 1

        for i in g:
            for k in d:
                if k >= i and d[k] > 0:
                    d[k] -= 1
                    c += 1
                    break

        return c
        