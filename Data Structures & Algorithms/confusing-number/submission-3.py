class Solution:
    def confusingNumber(self, n: int) -> bool:
        
        n = str(n)
        print(n)

        a = ['0', '1', '6', '8', '9']
        out = deque()

        for c in n:
            if c not in a:
                return False

            if c == '6':
                out.appendleft('9')
            elif c == '9':
                out.appendleft('6')
            else:
                out.appendleft(c)
        
        new = ""
        for c in out:
            new += c
        
        if new == n:
            return False
        return True

