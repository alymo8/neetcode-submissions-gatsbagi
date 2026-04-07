# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # if not list1 and not list2:
        #     return None
        # elif not list1:
        #     return list2
        # elif not list2:
        #     return list1

        # head = None
        # if list1.val > list2.val:
        #     head = list2
        #     list2 = list2.next
        # else:
        #     head = list1
        #     list1 = list1.next
        head = ListNode()
        it = head
        cur1 = list1
        cur2 = list2
        while cur1 != None and cur2 != None:
            if cur2.val <= cur1.val:
                it.next = cur2
                cur2 = cur2.next
            elif cur2.val > cur1.val:
                it.next = cur1
                cur1 = cur1.next
            it = it.next
        if cur1:
            it.next = cur1
        elif cur2:
            it.next = cur2
        return head.next
