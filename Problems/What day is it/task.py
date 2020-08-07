offset = int(input())
ref_time = 10.5
check = ref_time + offset
if check < 0:
    print('Monday')
elif check > 24:
    print('Wednesday')
else:
    print('Tuesday')
