class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        m = 0
        
        while k > 0:
            gifts.sort()
            gifts[-1] = floor(sqrt(gifts[-1]))
            k -= 1

        for g in gifts:
            m += g

        return m
            
        


