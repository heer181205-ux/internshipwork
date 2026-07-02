f1 = open("data.txt", "r")
f2 = open("backup.txt", "w")

f2.write(f1.read())

f1.close()
f2.close()