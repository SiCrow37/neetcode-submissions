# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if head is not None and head.val == val:
            while head.val == val:
                if head.next is not None:
                    head = head.next
                else:
                    return None
        
        cur = head

        while cur != None:
            if cur.next == None:
                return head
            elif cur.next.val == val:
                last = cur
                while cur.next is not None and cur.next.val == val:
                    cur = cur.next
                last.next = cur.next
            cur = cur.next
        return head

