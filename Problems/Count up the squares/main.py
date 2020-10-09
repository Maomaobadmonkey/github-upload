# put your python code here
# if first integer = 0, print 0
# create a list of numbers that are input until the result is 0
# if the list of numbers are 0 take the total amount of numbers and output the sum of the squares


integers = []
while True:
    integer = int(input())
    integers.append(integer)
    if sum(integers) == 0:
        break
print(sum(integer ** 2 for integer in integers))