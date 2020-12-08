txt = open('words.txt')

for line in txt:
    word = line.strip()
    print(len(word))
    if len(word) > 20:
        print(word)
