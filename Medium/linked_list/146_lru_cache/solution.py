class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.keys.get(key, None)
        if not node:
            return -1

        self._extract_node(node)

        self._append_tail(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.keys.get(key, None)
        if node:
            self._extract_node(node)

        node = Node(key, value)
        self.keys[key] = node

        self._append_tail(node)

        if len(self.keys) > self.capacity:
            node = self.head.next
            self._extract_node(node)
            del self.keys[node.key]

    def _extract_node(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def _append_tail(self, node) -> None:
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node
        return
