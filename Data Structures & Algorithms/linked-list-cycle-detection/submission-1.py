# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer1 = head
        pointer2 = head

        while pointer1 != None and pointer2 != None:
            pointer1 = pointer1.next
            if pointer2.next != None:
                pointer2 = pointer2.next.next
            else:
                return False

            if pointer1 == pointer2:
                return True
        return False
        