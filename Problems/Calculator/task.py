num1 = float(input())  # put your python code here
num2 = float(input())
operator = input()

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "pow":
    print(num1 ** num2)
elif num2 != 0.0 and operator == "mod":
    print(num1 % num2)
elif num2 != 0.0 and operator == "div":
    print(num1 // num2)
elif num2 != 0.0 and operator == "/":
    print(num1 / num2)
else:
    print("Division by 0!")
