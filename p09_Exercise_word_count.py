def word_count(s):
    if not s:
        return 0
    words = s.split()
    return len(words)