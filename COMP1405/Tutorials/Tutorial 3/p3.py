#1

print("Please write a paragraph and hit enter when you're finished")
writing = input()

#2

totalWords = writing.split(' ')

#3

totalSen = writing.split('.')
totalSen.pop(-1)

#4

print(f"Total number of words = {len(totalWords)}")
print(f"Total number of senteces = {len(totalSen)} \n")
print("Capitlized senteces are:")
num = 0
for e in totalSen:
    words = e.split(' ')
    firstWord = words[num]
    words.pop(num)
    words.insert(0, (firstWord[:1:].upper() + firstWord[1::]))
    if num == 1:
        words.pop(num)
    print(' '.join(words) + '.')
    num = 1
#hello, here are some words. and some sentences. you can count them.