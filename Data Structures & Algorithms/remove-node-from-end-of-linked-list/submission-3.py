# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        i = 0

        while cur:
            cur = cur.next
            i+=1
            
        index = i - n
        prev = ListNode()
        prev.next = head
        first = prev
        cur = head
        i = 0
        while cur:
            if i == index:
                cur = cur.next 
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
            i += 1
        return first.next

        

