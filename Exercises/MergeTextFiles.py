import datetime as dt
r"""

    This script reads the contents of three files and
    merges them into another file, whose name is the
    current time stamp.

"""
files = ["file1.txt", "file2.txt", "file3.txt"]
new_file = dt.datetime.now().strftime("%Y-%m-%d-%H-%M") + ".txt"

with open(new_file, "w+") as write_file:
    content = ""

    for file in files:
        with open(file, "r") as read_file:
            content += read_file.read()

    write_file.write(content)
