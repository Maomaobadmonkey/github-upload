funds = int(input())

if funds >= 6769:
    print(funds // 6769, " sheep")

elif funds >= 3848:
    buy = funds // 3848
    if buy != 1:
        print(funds // 3848, " cows")
    else:
        print(funds // 3848, " cow")

elif funds >= 1296:
    buy = funds // 1296
    if buy != 1:
        print(funds // 1296, " pigs")
    else:
        print(funds // 1296, " pig")

elif funds >= 678:
    buy = funds // 678
    if buy != 1:
        print(funds // 678, " goats")
    else:
        print(funds // 678, " goat")

elif funds >= 23:
    buy = funds // 23
    if buy != 1:
        print(funds // 23, " chickens")
    else:
        print(funds // 23, " chicken")
else:
    print('None')
