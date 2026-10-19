# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow = head,head
        while fast and fast.next:
            slow= slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            res= head
        while prev:
            temp2 = head.next
            head.next = prev
            temp3 = prev.next
            prev.next = temp2
            prev = temp3
            head = temp2



        