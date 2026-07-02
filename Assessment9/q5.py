f = open("data.txt", "a")

a = ["Apple", "Banana", "Mango"]

for i in a:
    f.write(i + "\n")

f.close()