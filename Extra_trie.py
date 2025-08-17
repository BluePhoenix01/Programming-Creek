class Node:
    def __init__(self):
        self.children = {}   # dictionary: char -> TrieNode
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def print_trie_tree(self):
        # Print the trie as a tree with indentation
        def _print(node, prefix):
            for char, child in node.children.items():
                print(prefix + '|-- ' + char)
                _print(child, prefix + '    ')
        _print(self.root, '')

word_list = [
    "apple", "app", "banana", "band", "bandana", "band"
]

trie = Trie()
for word in word_list:
    trie.insert(word)

print("Trie contains 'app':", trie.search("app"))  # True
print("Trie contains 'apple':", trie.search("apple"))  # True

print("Trie Tree Representation:")
trie.print_trie_tree()