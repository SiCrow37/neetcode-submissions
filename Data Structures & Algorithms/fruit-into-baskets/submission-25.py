class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        largest = 0

        for i in range(len(fruits)):
            t = 0
            b1 = -1
            b2 = -1

            for f in range(i, len(fruits)):
                if b1 == -1:
                    b1 = fruits[f]
                    t += 1
                    continue

                if fruits[f] == b1:
                    t += 1
                    continue

                if b2 == -1:
                    b2 = fruits[f]
                    t += 1
                    continue

                if fruits[f] == b2:
                    t += 1
                    continue

                if fruits[f] != b2 and fruits[f] != b1:
                    break

            if t > largest: 
                largest = t
        
        return largest
            

            