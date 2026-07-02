word = "Python"

f = open("data.txt", "r")

for i in f:
    if word in i:
        print(i)

f.close()