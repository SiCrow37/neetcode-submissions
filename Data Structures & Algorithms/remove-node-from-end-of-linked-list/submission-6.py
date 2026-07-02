# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = {}
        cur = head
        i = 1
        last = -1


        while cur:
            d[i] = cur
            last = i
            cur = cur.next
            i += 1
        print(last)

        if last == 1:
            head = None
            return head

        if last - n == 0:
            return head.next
        
        i = 1
        cur = head
        while cur:
            if i == last - n:
                cur.next = cur.next.next

            cur = cur.next
            i += 1

        return head
        