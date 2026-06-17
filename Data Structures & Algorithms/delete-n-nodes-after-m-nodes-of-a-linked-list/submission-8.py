# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        cur = head
        mm = m
        nn = n

        while cur is not None:

            if mm > 1:
                if cur.next is None:
                    return head
                cur = cur.next
                mm -= 1

            elif mm == 1:
                if nn == 0:
                    mm = m
                elif nn > 0:
                    while nn > 0:
                        if cur.next is not None:
                            cur.next = cur.next.next
                            nn -= 1
                        else:
                            return head
                    mm = m
                    nn = n
                    cur = cur.next

        return head
            


                
