income = int(input())

if income >= 132407:
    percent = 28
    calculated_tax = round(income * .28)
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')

elif income >= 42708:
    percent = 25
    calculated_tax = round(income * .25)
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')

elif income >= 15528:
    percent = 15
    calculated_tax = round(income * .15)
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')

else:
    percent = 0
    calculated_tax = 0
    print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')