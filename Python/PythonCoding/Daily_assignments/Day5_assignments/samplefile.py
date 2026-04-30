
line_count = 0
word_count = 0
char_count = 0


with open('sample.txt', 'r') as file:
    for line in file:
        line_count += 1
        words = line.split()
        word_count += len(words)
        char_count += len(line)

print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Number of characters:", char_count)