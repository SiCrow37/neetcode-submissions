class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = dict()
        count = 0
        
        for num in arr:
            if num in seen:
                seen[num] = seen[num] + 1
            if num not in seen:
                seen[num] = 1
        for item in seen:
            if item +1 in seen:
                count += seen[item]
        return count
                