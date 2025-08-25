from Extra_trees import BinaryTree

class TreeTraversalRecursive:
    def __init__(self):
        self.tree = BinaryTree()

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.val, end=" ")
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.val, end=" ")

class TreeTraversalIterative:
    def __init__(self, bt):
        self.tree = bt

    def preorder_traversal(self):
        current = self.tree.root
        stack = [current]
        while stack:
            node = stack.pop()
            print(node.val, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def inorder_traversal(self):
        current = self.tree.root
        stack = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.val, end=" ")
            current = current.right
    
    def postorder_traversal(self):
        current = self.tree.root
        stack = []
        last_visited = None
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack[-1]
                if node.right and last_visited != node.right:
                    current = node.right
                else:
                    print(node.val, end=" ")
                    last_visited = stack.pop()

class BSTIteratorPreorder:
    def __init__(self, root):
        self.stack = [root] if root else []

    def next(self):
        if not self.hasNext():
            return None
        node = self.stack.pop()
        if node.right:
            self.stack.append(node.right)
        if node.left:
            self.stack.append(node.left)
        return node.val

    def hasNext(self):
        return len(self.stack) > 0

class BSTIteratorInorder:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        val = node.val
        if node.right:
            self._push_left(node.right)
        return val
    
    def hasNext(self):
        return len(self.stack) > 0          

class BSTIteratorPostorder:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)
        self.last_visited = None

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        while self.hasNext():
            node = self.stack[-1]
            if node.right and self.last_visited != node.right:
                self._push_left(node.right)
            else:
                self.last_visited = self.stack.pop()
                return node.val
        
    def hasNext(self):
        return len(self.stack) > 0

#example usage
if __name__ == "__main__":
    bt = BinaryTree(10)
    bt.add_leaf(5)
    bt.add_leaf(15)
    bt.add_leaf(3)
    bt.add_leaf(7)
    bt.add_leaf(12)
    bt.add_leaf(18)

    print("Tree structure:")
    bt.print_tree()

    # print("Recursive Preorder Traversal:")
    # ttr = TreeTraversalRecursive()
    # ttr.tree = bt
    # ttr.preorder_traversal(bt.root)
    # print("\n")
    # print("Recursive Inorder Traversal:")
    # ttr.inorder_traversal(bt.root)
    # print("\n")
    # print("Recursive Postorder Traversal:")
    # ttr.postorder_traversal(bt.root)
    # print("\n")

    # print("Iterative Preorder Traversal:")
    # tti = TreeTraversalIterative(bt)
    # tti.preorder_traversal()
    # print("\n")

    # print("Iterative Inorder Traversal:")
    # tti.inorder_traversal()
    # print("\n")

    # print("Iterative Postorder Traversal:")
    # tti.postorder_traversal()
    # print("\n")

    print("BST Iterator Preorder:")
    bst_Preorder_iterator = BSTIteratorPreorder(bt.root)
    while bst_Preorder_iterator.hasNext():
        print(bst_Preorder_iterator.next(), end=" ")
    print("\n")
    print("BST Iterator Inorder:")
    bst_IOiterator = BSTIteratorInorder(bt.root)
    while bst_IOiterator.hasNext():
        print(bst_IOiterator.next(), end=" ")
    print("\n")
    print("BST Iterator Postorder:")
    bst_Postorder_iterator = BSTIteratorPostorder(bt.root)
    while bst_Postorder_iterator.hasNext():
        print(bst_Postorder_iterator.next(), end=" ")
    print("\n")
