# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        d = {}
        d2 = {}

        cur = head

        while cur is not None:
            if cur.val not in d:
                d[cur.val] = 1
            else:
                d[cur.val] += 1
            cur = cur.next
        print(d)
        
        cur = head
        
        while cur is not None:
            if cur.val in d and d[cur.val] == 1:
                d2[cur] = 1
            cur = cur.next
        print(d2)

        if len(d2) == 0:
            head = None
            return head

        new = ListNode(None)
        cur = new


        for k in d2:
            cur.next = k
            cur = cur.next
            
        cur.next = None

        return new.next


        