file = open("example.txt", "r")
content = file.read()
print(content)
file.seek(0)
content = file.readlines()
content = [i.rstrip("\n") for i in content]
print(content)
