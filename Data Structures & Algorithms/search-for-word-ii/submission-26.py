class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]    
        cur.endOfWord = True
    
    def search(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        
        return cur.endOfWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        res = []
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, node, word):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited
            ):
                return
            ch = board[r][c]

            if ch not in node.children:
                return
            
            visited.add((r, c))
            word += ch
            if node.children[ch].endOfWord:
                res.append(word)
                node.children[ch].endOfWord = False

            dfs(r + 1, c, node.children[ch], word)
            dfs(r, c + 1, node.children[ch], word)
            dfs(r - 1, c, node.children[ch], word)
            dfs(r, c - 1, node.children[ch], word)

            visited.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")
    
        return res
        