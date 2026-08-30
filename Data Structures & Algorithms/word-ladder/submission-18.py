class Solution:
    def isAllowed(self, s, t):
        count = 0

        for i in range(len(s)):
            if s[i] != t[i]:
                count += 1

        return count == 1
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])
        visited = set()

        if endWord not in wordList:
            return 0

        step = 0
        while q:
            step += 1
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node == endWord:
                    return step

                if node in visited:
                    continue
                
                visited.add(node)
                for w in wordList:
                    if w not in visited and self.isAllowed(node, w):
                        q.append(w)
        return 0