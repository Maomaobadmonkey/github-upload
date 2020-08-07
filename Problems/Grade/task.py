score = int(input())
maximum = int(input())
percentage = float(score / maximum) * 100
if percentage < 60:
    print("F")
elif 60 <= percentage < 70:
    print("D")
elif 70 <= percentage < 80:
    print("C")
elif 80 <= percentage < 90:
    print("B")
elif 90 <= percentage <= 100:
    print("A")