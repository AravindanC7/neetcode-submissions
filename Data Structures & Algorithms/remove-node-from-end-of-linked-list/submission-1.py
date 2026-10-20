# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # 1. Reverse the entire list
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 'prev' is now the new head of the reversed list
        reversed_head = prev

        # 2. Remove the N-th node from the front of the reversed list
        # Dummy node handles removing the 1st node of reversed list (which is the last node of original)
        dummy = ListNode(0, reversed_head)
        curr = dummy

        # Advance curr to the node right BEFORE the one we want to remove
        for _ in range(n - 1):
            curr = curr.next

        # Unlink the target node
        curr.next = curr.next.next

        # 3. Reverse the list back to its original order
        prev2 = None
        curr1 = dummy.next
        while curr1:
            temp2 = curr1.next
            curr1.next = prev2
            prev2 = curr1
            curr1 = temp2

        return prev2