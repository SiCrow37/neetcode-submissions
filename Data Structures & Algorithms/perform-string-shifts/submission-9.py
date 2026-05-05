class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s = deque(s)
        for item in shift:
            a = item[1]
            if item[0] == 0:
                while a > 0:
                    s.append(s.popleft())
                    a -= 1

            elif item[0] == 1:
                while a > 0:
                    s.appendleft(s.pop())
                    a -= 1
        string = "".join(s)
        

        return string