class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = -1

        if needle in haystack:
            n = haystack.index(needle)
        
        return n