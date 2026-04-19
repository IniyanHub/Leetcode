class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0


class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}  # stores actual key values

    def insert(self, key: str, val: int) -> None:
        # Find difference (important for updates)
        diff = val - self.map.get(key, 0)
        self.map[key] = val

        node = self.root
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.score += diff

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.score