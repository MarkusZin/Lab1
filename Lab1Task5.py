word = ''
line = ''

while word != '.':
    word = input('Write a word: ')

    line += word
    if word != '.':
        line += ', '
    else:
        line = line[:len(line)-3] + word
print (line)