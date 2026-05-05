class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l = len(nums)
        i = 1
        j = 0
        dec = False
        inc = False
        equ = False

        if l == 1:
            return True

        if nums[j] == nums[-1]:
            equ = True
        elif nums[j] < nums[-1]:
            inc = True
        elif nums[j] > nums[-1]:
            dec = True

        while i < l:
            if equ == True and nums[i] != nums[j]:
                return False
            elif inc == True and nums[i] < nums[j]:
                return False
            elif dec == True and nums[i] > nums[j]:
                return False
            i += 1
            j += 1
        return True



