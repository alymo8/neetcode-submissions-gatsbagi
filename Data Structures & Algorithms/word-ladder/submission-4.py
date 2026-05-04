class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        adj_list = {}

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj_list.setdefault(pattern, []).append(word)

        q = deque([beginWord])            
        visited = set([beginWord])
        res = 1


        while q:
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    neighbors = adj_list.get(pattern, [])
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
                            if neighbor == endWord:
                                return res + 1
            res += 1
        return 0