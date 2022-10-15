from forex_python.converter import CurrencyRates
c = CurrencyRates()
from_currency = input("From Currency Code: ").upper()
to_currency = input("To Currency Code: ").upper()
amount = int(input("Enter the amount that you want to convert from "+str(from_currency)+" to "+str(to_currency)+" : "))

result = c.convert(from_currency, to_currency, amount)
print("The Converted amount"+" in "+str(to_currency)+" is : ",result);