import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        word_set = set(wordList)
        while queue:
            current_word, steps = queue.popleft()
            for i in range(len(current_word)):
                for c in string.ascii_lowercase:
                    neighbor = current_word[:i] + c + current_word[i+1:]
                    if neighbor in word_set:
                        if neighbor == endWord:
                            return steps + 1
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append((neighbor, steps+1))
        return 0
