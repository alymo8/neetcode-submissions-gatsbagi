# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur is not None:
            # cur has to go to next
            # prev has to take the value of cur
            # cur.next has to point to prev

            inter = cur.next
            cur.next = prev
            prev = cur
            cur = inter

        return prev
           


        