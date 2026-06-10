class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = {}
        extra = []

        for n in arr1:
            if n not in d and n in arr2:
                d[n] = 1
            elif n in d: 
                d[n] += 1
            elif n not in arr2:
                extra.append(n)
        
        extra.sort()

        arr1 = []

        for n in arr2:
            while d[n] > 0:
                arr1.append(n)
                d[n] -= 1
        
        for n in extra:
            arr1.append(n)

        return arr1
        
