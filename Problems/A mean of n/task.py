n = int(input())
numlist = []

for _ in range(n):
    nums = int(input())
    numlist.append(nums)
count = len(numlist)
print(sum(numlist) / count)