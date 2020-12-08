txt = open('words.txt')
for line in txt:
    if 'e' not in line:
        print(line)
        
