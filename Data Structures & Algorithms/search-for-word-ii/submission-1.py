class Node:
    def __init__(self):
        self.children = {}
        self.marked = False

class Trie:
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.marked = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = Trie()
        visited = set()
        res = set()
        for word in words:
            trie.addWord(word)
            
        def dfs(r, c, node, word):
            if r < 0 or r == rows or  c < 0 or c == cols or (r, c) in visited or board[r][c] not in node.children:
                return
            
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.marked:
                res.add(word)

            visited.add((r, c))
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, trie.root, "")
        return list(res)

            