def make_dubsted_remix():
    vasya_words = input().split('WUB')
    remix_words = []
    for i in vasya_words:
        if i != '':
            remix_words.append(i)

    print(' '.join(remix_words))


make_dubsted_remix()
