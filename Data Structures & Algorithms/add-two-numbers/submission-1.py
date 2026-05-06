# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2

        res_root = ListNode()
        res = res_root
        carry = 0
        while cur1 or cur2 or carry == 1:
            val = 0
            if cur1: 
                val += cur1.val
                cur1 = cur1.next
            if cur2: 
                val += cur2.val
                cur2 = cur2.next
            val += carry
            carry = 0
            
            if val >= 10:
                res.next = ListNode(val - 10)
                carry = 1
            else:
                res.next = ListNode(val)
            res = res.next
        
        if cur1:
            res.next = cur1
        elif cur2:
            res.next = cur2
            # res.next 
        return res_root.next