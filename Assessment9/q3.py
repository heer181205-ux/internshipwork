f = open("data.txt", "r")
text = f.read().split()
f.close()

for i in set(text):
    print(i, text.count(i))