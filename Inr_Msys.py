def stem_words(text):
    words = text.split()
    stemmed_words = []
    for word in words:
        if word.endswith('ed') or word.endswith('ly'):
            stemmed_word = word[:-2]
        if word.endswith('ing'):
            stemmed_word = word[:-3]
        else:
            stemmed_word = word
        if len(stemmed_word) > 8:
            stemmed_word = stemmed_word[:8]
        stemmed_words.append(stemmed_word)
    return ' '.join(stemmed_words)


print(stem_words("an extremely dangerous dog is barking"))
