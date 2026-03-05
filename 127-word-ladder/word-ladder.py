class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        
        # If endWord is not in the list, transformation is impossible
        if endWord not in word_set:
            return 0

        # Initialize queue with (current_word, current_path_length)
        queue = deque([(beginWord, 1)])
        
        # Keep track of visited words to prevent cycles
        visited = set([beginWord])

        while queue:
            current_word, level = queue.popleft()

            # If we reached the endWord, return the length of the path
            if current_word == endWord:
                return level

            # Try changing every character in the word
            for i in range(len(current_word)):
                # Try every letter from 'a' to 'z'
                for char in string.ascii_lowercase:
                    # Skip if the character is the same as the original
                    if char == current_word[i]:
                        continue
                    
                    # Construct the new word
                    next_word = current_word[:i] + char + current_word[i+1:]

                    # If the new word is valid and not visited
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
        
        # If queue is empty and endWord not found
        return 0
        