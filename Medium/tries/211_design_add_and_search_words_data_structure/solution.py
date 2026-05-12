class Node:
    def __init__(
        self,
    ):
        self.next_letter = 26 * [None]
        self.is_word = False


class WordDictionary:
    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        node = self.head
        for letter in word:
            c = ord(letter) - 97

            if not node.next_letter[c]:
                node.next_letter[c] = Node()
            node = node.next_letter[c]

        node.is_word = True

        return

    def search(self, word: str) -> bool:
        def search_substr(node: Node, word: str, start_idx: int = 0):
            for idx in range(start_idx, len(word)):
                letter = word[idx]

                if letter != ".":
                    c = ord(letter) - 97

                    if not node.next_letter[c]:
                        return False

                    node = node.next_letter[c]
                else:
                    for elem in node.next_letter:
                        if elem and search_substr(elem, word, idx + 1):
                            return True

                    return False

            return node.is_word

        return search_substr(self.head, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
