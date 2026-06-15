class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        md = {}

        for ch in magazine:
            if ch not in md:
                md[ch] = 1
            else:
                md[ch] += 1
        
        for ch in ransomNote:
            if ch not in md:
                return False
            else:
                md[ch] -= 1
        
        for k in md:
            if md[k] < 0:
                return False
        
        return True