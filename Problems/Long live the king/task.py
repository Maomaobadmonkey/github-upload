col = int(input())
row = int(input())

if col in (1, 8) and row in (1, 8):
    print(3)

elif col in (1, 8) and (row > 1 or row < 8):
    print(5)

elif row in (1, 8) and (col > 1 or col < 8):
    print(5)

else:
    print(8)
