class Node:
    def __init__(self, value):
        self.value = value
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word: str) -> None:
        node = self.head
        for letter in word:
            if not letter in node.children.keys():
                node.children[letter] = Node(letter)
            node = node.children[letter]
        node.children["END"] = True

    def search(self, word: str) -> bool:
        node = self.head
        for letter in word:
            if not letter in node.children.keys():
                return False
            node = node.children[letter]
        return "END" in node.children

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for letter in prefix:
            if not letter in node.children.keys():
                return False
            node = node.children[letter]
        return True
