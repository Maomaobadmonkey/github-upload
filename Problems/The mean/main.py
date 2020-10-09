numlist = []

while True:
    number = input()
    if number != '.':
        numlist.append(int(number))
    else:
        mean = sum(numlist) / len(numlist)
        print(float(mean))
        break