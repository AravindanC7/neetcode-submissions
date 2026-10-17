# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        val1 = list1
        val2= list2
        while val1 and val2:
            if val1.val <= val2.val:
                curr.next = val1
                val1= val1.next
            else:
                curr.next  = val2
                val2=val2.next
            curr = curr.next
        if  val1:
            curr.next =val1
        else:
            curr.next = val2
        return dummy.next



        