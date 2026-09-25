class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def isAllowed(x, y):
            count = 0
            for i in range(len(x)):
                if x[i] != y[i]:
                    count += 1
            
            return count == 1
        
        q = deque([beginWord])
        visited = set()

        steps = 0
        while q:
            steps += 1
            size = len(q)
            for i in range(size):
                n = q.popleft()
                if n in visited:
                    continue
                
                visited.add(n)
                if n == endWord:
                    return steps
                
                for word in wordList:
                    if word not in visited and isAllowed(word, n):
                        q.append(word)
        
        return 0