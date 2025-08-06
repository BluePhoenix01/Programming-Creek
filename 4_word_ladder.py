def is_word_ladder(start, end, dict):
    visited = set()
    queue = [(start, 1)]
    while queue:
        word, level = queue.pop(0)
        if word == end:
            return level
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i + 1:]
                if new_word in dict and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, level + 1))
    return 0


print(is_word_ladder('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))                    