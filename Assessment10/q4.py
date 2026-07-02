balance = int(input("Enter balance: "))
amount = int(input("Enter amount: "))

if amount <= balance:
    print("Withdrawal Successful")
else:
    print("Insufficient Balance")