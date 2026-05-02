# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head == None:
            return
        # find middle
        size = 0
        prev = None
        cur = head
        while cur:
            size += 1
            prev = cur
            cur = cur.next
        
        mid = (size+1)//2
        i = 0
        cur = head
        while i < mid-1:
            i+=1
            cur = cur.next
        
        # split lists
        second = cur.next
        cur.next = None

        # reverse 2nd half
        prev = None
        while second:
            inter = second.next
            second.next = prev
            prev = second
            second = inter
        
        second = prev
        cur = head

        # merge 2 halves
        while second:
            inter1 = cur.next
            inter2 = second.next

            cur.next = second
            second.next = inter1

            cur = inter1
            second = inter2

