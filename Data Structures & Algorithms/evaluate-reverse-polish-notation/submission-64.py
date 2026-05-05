class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s1 = []
        
        for t in tokens:
            if t.isdigit() or t.lstrip("-").isdigit():
                if not t.isdigit():
                    s1.append(int(t))
                else: s1.append(int(t))
                print(f"\ndigit: {t}")
                print(s1)
                    
            else:
                b = s1.pop()
                a = s1.pop()
                c = 0

                # calculations
                if t == '+':
                    c = a + b
                
                elif t == '-':
                    c = a - b
                
                elif t == '*':
                    c = a * b
                
                elif t == '/':
                    if abs(a) < abs(b):
                        c = 0
                    else:
                        if (a > 0 and b < 0) or (a < 0 and b > 0):
                            c = a / b
                            c = int(c * 1)

                        else:
                            c = a // b
                    
    

                        
                        

                # restack answer & remove last operand
                s1.append(c)
                print(f"\noperand: {t}")
                print(f"{a} {t} {b} = {c}")
                print(s1)

        return s1[0]

            
