# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # cur -> next
        # newcur go to next
        # newcur.next = prev
        prev = None
        cur = head
        while cur != None:
           inter = cur.next
           cur.next = prev
           prev = cur
           cur = inter
           if cur == None:
            return prev
           


        