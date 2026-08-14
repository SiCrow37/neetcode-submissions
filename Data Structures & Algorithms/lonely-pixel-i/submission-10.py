class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
        p = picture
        count = 0

        rows = len(p)
        cols = len(p[0])

        for i in range(len(p)):
            cr = p[i]
            for j in range(len(cr)):
                cc = [p[k][j] for k in range(len(p))]

                if p[i][j] == "B" and cr.count("B") == 1 and cc.count("B") == 1:
                    count += 1

        return count

                


                     
                    