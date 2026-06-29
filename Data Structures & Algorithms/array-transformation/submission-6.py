class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        changed = True


        while changed:
            changed = False
            up = []
            down = []
            
            for i in range(1, len(arr) - 1):
                if arr[i-1] > arr[i] and arr[i] < arr[i+1]:
                    up.append(i)
                    changed = True
                elif arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                    down.append(i)
                    changed = True
            for x in up:
                arr[x] += 1
            for x in down:
                arr[x] -= 1
        
        return arr
