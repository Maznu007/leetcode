# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head
        leng = 1
        cur = head
        while cur.next!= None:
            cur = cur.next
            leng+=1
        cur.next = head
        k = k%leng
        steps = leng - k
        ntail = cur
        while steps:
            ntail = ntail.next
            steps-=1
        nhead = ntail.next
        ntail.next = None
        return nhead