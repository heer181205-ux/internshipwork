f = open("data.txt", "r")
text = f.read()
f.close()

text = text.replace("Python", "Java")

f = open("data.txt", "w")
f.write(text)
f.close()