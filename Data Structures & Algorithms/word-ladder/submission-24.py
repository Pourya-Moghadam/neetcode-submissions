class Solution:
    def isAllowed(self, s, t):
        count = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                count += 1
        return count == 1
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])    
        step = 0
        visited = set()
        
        if endWord not in wordList:
            return 0
            
        while q:
            step += 1
            size = len(q)
            for i in range(size):
                curWord = q.popleft()
                if curWord == endWord:
                    return step
                
                if curWord in visited:
                    continue
                
                visited.add(curWord)

                for neiWord in wordList:
                    if neiWord not in visited and self.isAllowed(neiWord, curWord):
                        q.append(neiWord)
            
        return 0