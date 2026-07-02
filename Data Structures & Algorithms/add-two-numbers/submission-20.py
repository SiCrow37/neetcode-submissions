# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        l3 = ListNode(-1)
        c3 = l3
        counter = 1

        while c1 is not None:
            print(f"\n\nRound {counter}")
            cur = c1.val

            if c2 is not None:
                cur += c2.val
            
            print(f"after 1st add: {cur}")
            
            if cur >= 10:
                c3.next = ListNode(cur % 10)
                print(f"c3.next = {c3.next.val}")
                c3 = c3.next

                cur //= 10
                print(f"remainder: {cur}")

                if c1.next is not None:
                    c1.next.val += cur
                    print(f"c1.next.val = {c1.next.val}")
                else:
                    c1.next = ListNode(cur)
                    print(f"c1.next = {c1.next.val}")
                
            else:
                c3.next = ListNode(cur)
                c3 = c3.next

            if c1 is not None:
                c1 = c1.next
        
            if c2 is not None:
                c2 = c2.next

            counter += 1

        if c1 is None and c2 is not None:
            c3.next = c2
            
        return l3.next

                