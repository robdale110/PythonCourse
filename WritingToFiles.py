# Creates and writes to empty file, doesn't add to existing file
file = open("example1.txt", "w")
file.write("Line 1")
file.close()
file = open("example1.txt", "w")
file.write("Line 2")
file.close()

line = ["Line 1", "Line 2", "Line 3"]
file = open("example1.txt", "w")
for item in line:
    file.write(item + "\n")
file.close()
