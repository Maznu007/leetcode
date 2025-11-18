# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        cur = slow
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        firsthalf = head
        secondhalf = prev
        while secondhalf:
            if firsthalf.val != secondhalf.val:
                return False
            firsthalf = firsthalf.next
            secondhalf = secondhalf.next
        return True