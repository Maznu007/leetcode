# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getkth(node,k):
            while node and k>0:
                node = node.next
                k-=1
            return node
        dummy = ListNode(0,head)
        groupprev = dummy
        while True:
            kth = getkth(groupprev,k)
            if not kth:
                break
            groupNext = kth.next
            prev = groupNext
            curr = groupprev.next

            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupprev.next
            groupprev.next = prev
            groupprev = temp
        return dummy.next        