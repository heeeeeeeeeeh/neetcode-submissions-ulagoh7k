class Node:
    def __init__(self, char, marked=False):
        self.char = char
        self.children = {}
        self.marked = marked
class PrefixTree:

    def __init__(self):
        self.root = Node("")
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]
        cur.marked = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.marked
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if  c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        