class Node:
    def __init__(self, char, marked=False):
        self.char = char
        self.children = [None]*26
        self.marked = marked
class PrefixTree:

    def __init__(self):
        self.root = Node("")
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            index = ord('a')-ord(c)
            if not cur.children[index]:
                cur.children[index] = Node(c)
            cur = cur.children[index]
        cur.marked = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            index = ord('a')-ord(c)
            if not cur.children[index]:
                return False
            cur = cur.children[index]
        return cur.marked
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            index = ord('a')-ord(c)
            if not cur.children[index]:
                return False
            cur = cur.children[index]
        return True
        