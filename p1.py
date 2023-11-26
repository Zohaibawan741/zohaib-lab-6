from collections import deque

def ladderLength(startWord, endWord, wordList):
    if endWord not in wordList or not endWord or not startWord or not wordList:
        return 0

    wordList, queue = set(wordList), deque([(startWord, 1)])

    while queue:
        current_word, length = queue.popleft()

        if current_word == endWord:
            return length

        queue.extend((next_word, length + 1) for next_word in list(wordList) if sum(c1 != c2 for c1, c2 in zip(current_word, next_word)) == 1)
        wordList -= set(queue[i][0] for i in range(len(queue)))

    return 0

startWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

result = ladderLength(startWord, endWord, wordList)
print(result)