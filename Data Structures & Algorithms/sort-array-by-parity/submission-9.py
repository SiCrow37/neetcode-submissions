class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = [n for n in nums if n % 2 == 1]
        even = [n for n in nums if n % 2 == 0]

        return even + odd
        