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
        i = 0
        cur = head
        while cur:
            i+=1
            cur = cur.next
        mid = (i+1) // 2

        # split lists from mid
        i = 0
        prev = None
        cur = head
        while i < mid:
            i+=1
            prev = cur
            cur = cur.next
            
        prev.next = None
        
        # reverse 2nd list
        
        prev = None
        while cur:
            inter = cur.next
            cur.next = prev
            prev = cur
            cur = inter

        second = prev
        # merge
        cur = head

        while second:
            inter1 = cur.next
            inter2 = second.next

            cur.next = second
            second.next = inter1

            cur = inter1
            second = inter2





