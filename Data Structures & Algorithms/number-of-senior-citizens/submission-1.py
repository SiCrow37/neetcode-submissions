class Solution:
    def countSeniors(self, details: List[str]) -> int:
        a = 0
        for d in details:
            if int(d[11]) < 6: continue
            if int(d[11]) == 6 and int(d[12]) == 0: continue
            else: a += 1
        return a

