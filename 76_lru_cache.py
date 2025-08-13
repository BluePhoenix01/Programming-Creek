class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node
    
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.dll = DoublyLinkedList()
    
    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.dll.remove_node(node)
        self.dll.add_to_head(node)
        return node.value
    
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.dll.remove_node(node)
            self.dll.add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                lru = self.dll.remove_tail()
                del self.cache[lru.key]
            new_node = Node(key, value)
            self.dll.add_to_head(new_node)
            self.cache[key] = new_node
    
lru_cache = LRUCache(2)

lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1))  # Output: 1
lru_cache.put(3, 3)      # Evicts key 2
print(lru_cache.get(2))  # Output: -1 (not found)