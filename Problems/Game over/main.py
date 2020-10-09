scores = input().split()
# put your python code here
# the user has 3 or more incorrect answers print "Game over"
# the code must track how many inputs are correct and how many are incorrect
# If the inputs do not reach the 3 lives threshold and complete the input cycle, print "You won"
# The user is also presented with how many correct answers they got correct before final i


correct = 0
incorrect = 0


for x in scores:
    if x == 'C':
        correct += 1
    elif x == 'I':
        incorrect += 1
        if incorrect >= 3:
            print('Game over')
            print(correct)
            break
else:
    print('You won')
    print(correct)