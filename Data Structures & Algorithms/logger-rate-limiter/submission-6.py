class Logger:

    def __init__(self):
        self.d = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        t = timestamp
        m = message

        print(f"\n\nt = {t}")
        print(f"m = {m}")
        print(f"next {m}: {t+10}")

        if m not in self.d:
            self.d[m] = t
            print(f"{m} added")
            return True
        else:
            if self.d[m] + 10 > t:
                print(f"{t} < {t + 10}: cant do it")
                return False
            else:
                print(f"old t: {t}")
                self.d[m] = t
                print(f"new t: {t}")
                return True

                
            
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
