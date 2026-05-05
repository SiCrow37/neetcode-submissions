class Solution:
    def trap(self, height: List[int]) -> int:
        
        # pointers from both ends
        # keep track of last max from both ends
        # overall maximum area
        m = 0

        # loop pointers
        lp = 0
        rp = len(height) - 1

        # last max heights
        last_l = 0
        last_r = 0

        # The core idea of the two-pointer approach for trapping rain water is:
        # At any point, the amount of water trapped is determined by the shorter of the two boundaries.
        # Instead of moving both pointers simultaneously, we move the pointer that points to a shorter bar.
        
        while lp <= rp:
            # If the left wall is shorter or equal to the right wall,
            # we know the water at lp is limited by last_l, not by whatever is beyond rp.
            if last_l <= last_r:
                if height[lp] >= last_l:
                    last_l = height[lp]
                else:
                    m += last_l - height[lp]
                lp += 1
            else:
                # If the right wall is shorter, water at rp is limited by last_r.
                if height[rp] >= last_r:
                    last_r = height[rp]
                else:
                    m += last_r - height[rp]
                rp -= 1
            
        return m