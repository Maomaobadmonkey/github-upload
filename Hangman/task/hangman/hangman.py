import random

print("H A N G M A N")  # Write your code here

random.seed()
guess_words = ['python', 'java', 'kotlin', 'javascript']
picker = random.choice(guess_words)
guess_p = picker.replace('hon', '--')
guess_j = guess_p.rstrip('a') + '-'
guess_k = guess_j.replace('lin', '--')
guess_ja = guess_k.replace('ascript', '------')
print(f'Guess the word {guess_ja}:')

word = input()

if word == picker:
    print('You survived!')

else:
    print('You are hanged!')
