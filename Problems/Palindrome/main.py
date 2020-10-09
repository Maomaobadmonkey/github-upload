word = list(input())

backword = []

for x in word:
    backword.append(x)

word.reverse()

if word == backword:
    print('Palindrome')
else:
    print('Not palindrome')