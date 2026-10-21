"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.c = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        dict1 ={}
        while curr:
            dict1[curr] = Node(curr.val)
            curr=curr.next
        new=head
        while new:
            dict1[new].next = dict1.get(new.next)
            dict1[new].random = dict1.get(new.random)
            new= new.next
        return dict1[head]
        