class Node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1 if val else 0

class BinaryTree:
    def __init__(self, val = None):
        self.root = Node(val)

    def add_leaf(self, val):
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            self._add_leaf(self.root, new_node)

    def _add_leaf(self, curr, new_node):
        print(f"Adding {new_node.val} to the tree")
        if curr is None:
            return new_node
        if new_node.val < curr.val:
            curr.left = self._add_leaf(curr.left, new_node)
        else:
            curr.right = self._add_leaf(curr.right, new_node)
        return curr

    def print_tree(self):
        #Print layer by layer
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
            current_level = [child for child in next_level if child]
        print()

class AVLTree:
    def __init__(self, val = None):
        self.head = Node(val)
        self.bf = 0

    def add_leaf(self, val):
        self.head = self._add_leaf(self.head, val)

    def _add_leaf(self, curr, val):
        if curr is None:
            return Node(val)
        if val < curr.val:
            curr.left = self._add_leaf(curr.left, val)
        else:
            curr.right = self._add_leaf(curr.right, val)
        return self._balance(curr)

    def _balance(self, curr):
        self.bf = self._get_balance_factor(curr)
        if self.bf > 1:
            if self._get_balance_factor(curr.left) < 0:
                curr.left = self._rotate_left(curr.left)
            return self._rotate_right(curr)

        if self.bf < -1:
            if self._get_balance_factor(curr.right) > 0:
                curr.right = self._rotate_right(curr.right)
            return self._rotate_left(curr)

        return curr

    def _get_balance_factor(self, curr):
        if curr is None:
            return 0
        return self._get_height(curr.left) - self._get_height(curr.right)

    def _get_height(self, curr):
        if curr is None:
            return 0
        return 1 + max(self._get_height(curr.left), self._get_height(curr.right))
    
    def _rotate_left(self, z):
        y = z.right
        z.right = y.left
        y.left = z
        return y

    def _rotate_right(self, z):
        y = z.left
        z.left = y.right
        y.right = z
        return y

    def delete(self, val):
        self.head = self._delete(self.head, val)

    def _delete(self, curr, val):
        if curr is None:
            return curr
        if val < curr.val:
            curr.left = self._delete(curr.left, val)
        elif val > curr.val:
            curr.right = self._delete(curr.right, val)
        else:
            # Node with only one child or no child
            if curr.left is None:
                return curr.right
            elif curr.right is None:
                return curr.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            min_larger_node = self._get_min(curr.right)
            curr.val = min_larger_node.val
            curr.right = self._delete(curr.right, min_larger_node.val)
        return self._balance(curr)

    def _get_min(self, curr):
        while curr.left is not None:
            curr = curr.left
        return curr

    def print_tree(self):
        # Print layer by layer
        if not self.head:
            return
        current_level = [self.head]
        while current_level:
            next_level = []
            for node in current_level:
                if node:
                    print(node.val, end=' ')
                    next_level.append(node.left)
                    next_level.append(node.right)
            print()
            current_level = [child for child in next_level if child]
        print()

# Balanced Tree
tree = AVLTree(0)
tree.add_leaf(1)
tree.add_leaf(2)
tree.add_leaf(3)
tree.add_leaf(4)
tree.add_leaf(5)

# Binary Tree
# tree = BinaryTree(0)
# tree.add_leaf(7)
# tree.add_leaf(2)
# tree.add_leaf(1)
# tree.add_leaf(3)
# tree.add_leaf(5)
# tree.add_leaf(4)

print("Binary Tree:")
tree.print_tree()