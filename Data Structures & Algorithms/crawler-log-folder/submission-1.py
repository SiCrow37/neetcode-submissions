class Solution:
    def minOperations(self, logs: List[str]) -> int:
        n = 0
        for l in logs:
            if l == "../":
                if n == 0:
                    continue
                n -= 1
            elif l == "./":
                continue
            else: n += 1
        
        return n
            