class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 0
        self.prev = None
        self.next = None

    def increment_count(self):
        self.count += 1

class DLList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        node.increment_count()

    def remove_head(self):
        """Remove and return the first real node (LFU eviction)."""
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove_node(first)
        return first

    def remove_node(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def remove_tail(self):
        if self.tail.prev == self.head:
            return None
        node = self.tail.prev
        self.remove_node(node)
        return node

    def order_by_count(self, node):
        while node.prev != self.head and node.count > node.prev.count:
            self.swap_with_prev(node)

    def swap_with_prev(self, node):
        prev = node.prev
        if prev == self.head:
            return
        prev.prev.next = node
        node.prev = prev.prev
        prev.prev = node
        node.next.prev = prev
        prev.next = node.next
        node.next = prev

    def is_empty(self):
        return self.head.next == self.tail
    
class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.dll = DLList()

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        node.increment_count()
        self.dll.order_by_count(node)
        return node.val

    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            node.increment_count()
            self.dll.order_by_count(node)
        else:
            if len(self.cache) >= self.capacity:
                lfu = self.dll.remove_tail()
                del self.cache[lfu.key]
            node = Node(key, value)
            self.cache[key] = node
            self.dll.add_to_tail(node)

class LFUCacheFreqMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.cache = {}      # key -> Node
        self.freq_map = {}   # freq -> DLList

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._update_freq(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._update_freq(node)
        else:
            if self.size >= self.capacity:
                # Evict least frequently used node
                lfu_list = self.freq_map[self.min_freq]
                to_remove = lfu_list.remove_head()
                del self.cache[to_remove.key]
                self.size -= 1

            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            if 1 not in self.freq_map:
                self.freq_map[1] = DLList()
            self.freq_map[1].add_to_tail(new_node)
            self.min_freq = 1
            self.size += 1

    def _update_freq(self, node):
        """Helper: move node to the next frequency list."""
        freq = node.count
        self.freq_map[freq].remove_node(node)

        if self.freq_map[freq].is_empty():
            del self.freq_map[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        node.count += 1
        if node.count not in self.freq_map:
            self.freq_map[node.count] = DLList()
        self.freq_map[node.count].add_to_tail(node)

# Example Output
# cache = LFUCache(2)

# cache.put(1, 1)   # Cache: {1=1}
# cache.put(2, 2)   # Cache: {1=1, 2=2}
# print(cache.get(1))   # returns 1, increases freq of key 1. Cache: {1=1(freq2), 2=2(freq1)}
# cache.put(3, 3)   # Evicts key 2 (LFU), adds key 3. Cache: {1=1(freq2), 3=3(freq1)}
# print(cache.get(2))   # returns -1 (not found)
# cache.put(4, 4)   # Evicts key 3 (LFU), adds key 4. Cache: {1=1(freq2), 4=4(freq1)}
# print(cache.get(3))   # returns -1 (not found)
# print(cache.get(4))   # returns 4, increases freq of key 4. Cache: {1=1(freq2), 4=4(freq2)}
# cache.put(5, 5)   # Both keys 1 and 4 freq=2, evicts least recently used (key 1), adds key 5. Cache: {4=4(freq2), 5=5(freq1)}

cache = LFUCacheFreqMap(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # returns 1
cache.put(3, 3)      # evicts key 2
print(cache.get(2))  # returns -1 (not found)




