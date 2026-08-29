class Node: 
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = Node()
            cur = cur.children[w]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add(w)
        
        res = set()
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, node, w):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return
            
            ch = board[r][c]
            w += ch
            node = node.children[ch]

            if node.isWord:
                res.add(w)

            visited.add((r, c))
            dfs(r + 1, c, node, w)
            dfs(r, c + 1, node, w)
            dfs(r - 1, c, node, w)
            dfs(r, c - 1, node, w)

            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")

        return list(res)




