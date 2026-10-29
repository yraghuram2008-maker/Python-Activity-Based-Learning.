units = int(input("Enter units: "))

if units <= 100:
    bill = units * 2
else:
    bill = 200 + (units - 100) * 5

print("Electricity Bill:", bill)
