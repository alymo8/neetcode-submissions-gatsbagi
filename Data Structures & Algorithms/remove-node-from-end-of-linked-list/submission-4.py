# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)

        cur, i = head, 0
        while cur:
            cur = cur.next
            i+=1
        index = i - n

        prev = dummy
        cur, i = head, 0
        while cur:
            if i == index:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
            i += 1
        return dummy.next



        

