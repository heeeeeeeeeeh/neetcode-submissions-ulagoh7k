class Node:
    def __init__(self, marked=False):
        self.marked = marked
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node("")
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if  c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.marked = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.marked
            
            if word[i] == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if not word[i] in node.children:
                    return False
                return dfs(node.children[word[i]], i + 1)
        return dfs(self.root, 0)
        
