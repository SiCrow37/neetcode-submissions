class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        t = len(words)
        for w in words:
            for ch in w:
                if ch not in allowed:
                    t -= 1
                    break
        return t