# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slower = head
        faster = head
        
        while faster != None and faster.next != None:
            slower = slower.next
            faster = faster.next.next
            
            if slower == faster:
                return True
            
        return False