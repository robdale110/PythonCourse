# Similar to using in c# closes file
with(open("example.txt", "a+")) as file: # a+ append and read
    file.seek(0)
    content = file.read()
    file.write("\nAnother line")

print(content)
