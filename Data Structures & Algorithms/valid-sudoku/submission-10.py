class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        v = dict()
        box1 = []
        box2 = []
        box3 = []

        for i in range(0, len(board)):
            if i == 3 or i == 6:
                box1 = []
                box2 = []
                box3 = []
            
            # create a new arr for each row
            h = []

            for j in range(0, len(board)):

                # checks boxes
                if j < 3 and board[i][j] != '.':
                    if board[i][j] not in box1:
                        box1.append(board[i][j])
                    else: return False
                elif j < 6 and j > 2 and board[i][j] != '.':
                    if board[i][j] not in box2:
                        box2.append(board[i][j])
                    else: return False
                elif j > 5 and board[i][j] != '.':
                    if board[i][j] not in box3:
                        box3.append(board[i][j])
                    else: return False


                if board[i][j] != '.':
                    if board[i][j] in h:
                        return False
                    else: 
                        h.append(board[i][j])


                    if j not in v:
                        v[j] = []
                        v[j].append(board[i][j])
                    else:
                        if board[i][j] in v[j]:
                            return False
                        else:
                            v[j].append(board[i][j])


        return True

                    

