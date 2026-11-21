# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        curr = dummyNode

        L = curr
        R = curr
        for i in range(n + 1):
            if R:
                R = R.next

        while R:
            L = L.next
            R = R.next

        L.next = L.next.next

        return dummyNode.next
                        
        