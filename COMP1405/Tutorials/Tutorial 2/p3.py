billAmount = float(input('Enter the bill amount:'))
tipPerc = float(input('Enter tip percentage:'))
tipAmount = (billAmount) * (tipPerc/100)
total = billAmount + tipAmount
print(f'A{tipPerc}% tip on a $ {billAmount} equals $ {tipAmount}')
print(f'The total bill is:{total}')