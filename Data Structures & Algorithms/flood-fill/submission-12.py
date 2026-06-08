class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = []
        original = image[sr][sc]
        visited = {}

        visited[(sr, sc)] = 1

        def addAdjacent(x, y):
            if x + 1 < len(image) and image[x+1][y] == original and [x+1, y] not in stack and (x+1, y) not in visited:
                stack.append([x+1, y])
                visited[(x+1, y)] = 1
            if x - 1 > -1 and image[x-1][y] == original and [x-1, y] not in stack and (x-1, y) not in visited:
                stack.append([x-1, y])
                visited[(x-1, y)] = 1
            if y + 1 < len(image[x]) and image[x][y+1] == original and [x, y+1] not in stack and (x, y+1) not in visited:
                stack.append([x, y+1])
                visited[(x, y+1)] = 1
            if y - 1 > -1 and image[x][y-1] == original and [x, y-1] not in stack and (x, y-1) not in visited:
                stack.append([x, y-1])
                visited[(x, y-1)] = 1
        
        addAdjacent(sr, sc)

        while len(stack) > 0:
            c = (stack[-1][0], stack[-1][1])
            stack.pop()
            addAdjacent(c[0], c[1])

        for p in visited:
            image[p[0]][p[1]] = color
        
        return image
