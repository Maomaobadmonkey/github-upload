import random

word_list = ['python', 'java', 'kotlin', 'javascript']

answer = random.choice(word_list)

correct_letters = set()


def show_word():
    word = ''
    for letter in answer:
        if letter in correct_letters:
            word += letter
        else:
            word += '-'
    print(word)


print('H A N G M A N')
print()

remainder_guess = 8
while remainder_guess > 0:
    show_word()
    input_letter = input(f'Input a letter: ')
    if input_letter in answer:
        correct_letters.update(input_letter)
    else:
        print('No such letter in the word')
    print()
    remainder_guess -= 1

print('Thanks for playing!')
print("We'll see how well you did in the next *stage")