# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        i = head
        r = None

        while i is not None:
            # add reversed list Node before the current head and point to the current one
            next_node = i.next
            i.next = r
            r = i
            
            # iterate i to the next node and make i equal the new node
            i = next_node

        return r