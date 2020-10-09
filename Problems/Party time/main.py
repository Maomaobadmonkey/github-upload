guestlist = []

while True:
    guest = input()
    guestlist.append(guest)
    if guest == '.':
        guestlist.pop(-1)
        print(guestlist)
        print(len(guestlist))
        break
