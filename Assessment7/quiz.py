score = 0

a = input("Capital of India: ")
if a.lower() == "delhi":
    score += 1

a = input("2 + 2 = ")
if a == "4":
    score += 1

a = input("Python is a programming language? (yes/no): ")
if a.lower() == "yes":
    score += 1

print("Score =", score)