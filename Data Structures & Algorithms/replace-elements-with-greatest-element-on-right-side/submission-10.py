class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_largest = 0
        largest = arr[-1]
        i = len(arr) - 1
        while i > -1:
            if arr[i] <= largest:
                arr[i] = largest
            if arr[i] > largest:
                new_largest = arr[i]
                arr[i] = largest
                largest = new_largest
            i -= 1

        arr[-1] = -1
        
        return arr
