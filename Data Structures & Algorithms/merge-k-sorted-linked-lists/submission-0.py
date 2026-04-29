# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        cur = float('inf')
        for node in lists:
            if node:
                cur = min(cur, node.val)
        for i, node in enumerate(lists):
            if node and node.val == cur:
                head = node
                lists[i] = lists[i].next
                break
        
        if not head:
            return None
        curnode = head

        finished = False
        while not finished:
            value = float('inf')
            finished = True
            for node in lists:
                if node:
                    finished = False
                    value = min(value, node.val)
            for i, node in enumerate(lists):
                if node and node.val == value:
                    curnode.next = node
                    curnode = curnode.next
                    lists[i] = lists[i].next
        return head