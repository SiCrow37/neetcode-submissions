class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        recorded = []
        low = 1

        while low <= high:
            mid = low + ((high - low) // 2)
            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)

            if total > h:
                low = mid + 1
            elif total <= h:
                recorded.append(mid)
                high = mid - 1
        if recorded:
            final = min(recorded)

        return final