class Node:
    def __init__(self,key: int=0,val: int=0):
        self.key = key
        self.val =val
        self.next = None
        self.prev = None
        

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def _add_node_(self,node : Node)->None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev=node
        self.head.next = node
    def _remove_node_(self,node : Node)->None:
        prev_node = node.prev
        next_node = node.next 
        prev_node.next = next_node
        next_node.prev = prev_node
    def _move_to_head_(self,node : Node)->None:
        self._remove_node_(node)
        self._add_node_(node)  
    def get(self, key: int) -> int:
        if key  not in self.cache:
            return -1
        node1 = self.cache[key]
        self._move_to_head_(node1)
        return node1.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node2=self.cache[key]
            node2.val = value
            self._move_to_head_(node2)     
        else:
            new_node = Node(key,value)
            self.cache[key] = new_node
            self._add_node_(new_node)
            if len(self.cache)> self.capacity:
                lru = self.tail.prev
                self._remove_node_(self.tail.prev)
                del self.cache[lru.key]

