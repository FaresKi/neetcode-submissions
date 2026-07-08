class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        word_set = set(wordList)
        print(f"word_set: {word_set}")
        while queue:
            current_word, steps = queue.popleft()
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    neighbor = current_word[:i] + c + current_word[i+1:]
                    if neighbor in word_set:
                        if neighbor == endWord:
                            print(f"neigbor: {neighbor} @ i: {i} and c: {c} and current_word: {current_word}")
                            return steps + 1
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append((neighbor, steps+1))
        return 0
