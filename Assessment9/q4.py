f = open("data.txt", "w")

for i in range(5):
    s = input()
    f.write(s + "\n")

f.close()