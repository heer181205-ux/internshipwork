a = int(input("First number: "))
b = int(input("Second number: "))
op = input("Enter + - * / : ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid Operator")