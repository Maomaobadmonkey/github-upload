word = input()
new_word = ""
for letter in word:
    if letter.isupper():
        new_word += "_{letter}".format(letter=letter.lower())
    else:
        new_word += letter

print(new_word)