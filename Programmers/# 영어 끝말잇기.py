def solution(n, words):
    already_told_words = set([])
    prev_word = words[0][0]
    for index, word in enumerate(words) :
        if word in already_told_words or not word.startswith(prev_word):
            return [(index%n)+1, int(index/n)+1]
        else :
            already_told_words.add(word)
            prev_word = word[-1]
    return [0, 0]