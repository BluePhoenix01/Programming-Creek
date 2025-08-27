class Heap:
    def __init__(self, min_heap=True):
        self.heap = []
        self.min_heap = min_heap

    def parent(self, i): return (i - 1)//2
    def left(self, i): return 2*i + 1
    def right(self, i): return 2*i + 2

    def _compare(self, a, b):
        return a < b if self.min_heap else a > b

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0 and self._compare(self.heap[i], self.heap[self.parent(i)]):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
        
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify(0)
        return root
    
    def _heapify(self, i):
        extreme = i
        l, r = self.left(i), self.right(i)

        if l < len(self.heap) and self._compare(self.heap[l], self.heap[extreme]):
            extreme = l
        if r < len(self.heap) and self._compare(self.heap[r], self.heap[extreme]):
            extreme = r
        if extreme != i:
            self.heap[i], self.heap[extreme] = self.heap[extreme], self.heap[i]
            self._heapify(extreme)

    def peek(self):
        return self.heap[0] if self.heap else None

# Example usage
if __name__ == "__main__":
    h = Heap(True)  # Min-heap
    h.push(5)
    h.push(3)
    h.push(8)
    print("Min element:", h.peek())
    print("Removed element:", h.pop())
    print("Min element after pop:", h.peek())

    h2 = Heap(False)  # Max-heap
    h2.push(5)
    h2.push(3)
    h2.push(8)
    print("Max element:", h2.peek())
    print("Removed element:", h2.pop())
    print("Max element after pop:", h2.peek())