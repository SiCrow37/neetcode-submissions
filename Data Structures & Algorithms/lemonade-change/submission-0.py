class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = defaultdict(int)

        for b in bills:
            if b == 5:
                d[5] += 1

            elif b == 10:
                d[10] += 1
                if d[5] < 1:
                    return False
                d[5] -= 1

            elif b == 20:
                d[20] += 1
                if d[10] >= 1:
                    d[10] -= 1
                    if d[5] >= 1:
                        d[5] -= 1
                        continue
                    return False
                elif d[10] == 0:
                    if d[5] >= 3:
                        d[5] -= 3
                        continue
                    return False
            
        return True
                    
            