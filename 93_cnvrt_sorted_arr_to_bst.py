class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

class BalancedTreeFromSortedArray:
    def __init__(self, sorted_array):
        self.root = self._sorted_array_to_bst(sorted_array)

    def _sorted_array_to_bst(self, sorted_array):
        if not sorted_array:
            return None
        mid = len(sorted_array) // 2
        root = Node(sorted_array[mid])
        root.left = self._sorted_array_to_bst(sorted_array[:mid])
        root.right = self._sorted_array_to_bst(sorted_array[mid + 1:])
        return root

    def print_tree(self):
        # Print layer by layer only till the last node
        if not self.root:
            return
        current_level = [self.root]
        while current_level:
            next_level = []
            for node in current_level:
                if node:
                    print(node.val, end=' ')
                    next_level.append(node.left)
                    next_level.append(node.right)
            print()
            current_level = next_level

tree = BalancedTreeFromSortedArray([1, 2, 3, 4, 5, 6, 7])
tree.print_tree()