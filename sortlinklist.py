# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        middle = self.getmiddle(head)
        nexttomiddle= middle.next
        middle.next = None
        left = self.sortList(head)
        right= self.sortList(nexttomiddle)
        return self.merge(left, right)

    def getmiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow =head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast =fast.next.next
            
        return slow
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy =ListNode(0)
        tail=dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
            
        return dummy.next