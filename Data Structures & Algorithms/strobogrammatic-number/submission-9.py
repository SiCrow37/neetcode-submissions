class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        l = 0
        r = len(num) - 1

        rev = ["0", "1", "8"]
        n = ["6", "9"]

        if l < r:
            while l < r:
                if num[l] not in rev and num[l] not in n: return False
                if num[r] not in rev and num[r] not in n: return False
                if num[l] in rev and num[r] != num[l]: return False
                if num[l] == "9" and num[r] != "6": return False
                if num[l] == "6" and num[r] != "9": return False
                l += 1
                r -= 1

        if l == r:
            if num[l] not in rev: return False
        
        return True

        