units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
else:
    bill = units * 8

print("Bill =", bill)