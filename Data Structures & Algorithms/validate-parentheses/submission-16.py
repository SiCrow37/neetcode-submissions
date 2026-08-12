class Solution:
    def isValid(self, s: str) -> bool:
        openers = ['(', '[', '{']
        closers = [')', ']', '}']
        stack = []

        for i in s:
            if i in openers:
                stack.append(i)
            if i in closers:
                if stack and stack[-1] == openers[0] and i == closers[0]:
                    stack.pop()
                elif stack and stack[-1] == openers[1] and i == closers[1]:
                    stack.pop()
                elif stack and stack[-1] == openers[2] and i == closers[2]:
                    stack.pop()
                else:
                    return False
        
        return not stack
        