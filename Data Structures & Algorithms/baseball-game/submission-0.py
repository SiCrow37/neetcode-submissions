class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        record = []
        for i in operations:
            if i == "D":
                record.append(2*record[-1])
                total += record[-1]
            elif i == "C":
                total -= record[-1]
                record.pop()
            elif i == "+":
                record.append(record[-1] + record[-2])
                total += record[-1]
            else: 
                record.append(int(i))
                total += record[-1]
                
        return total