import datetime
r"""

    This script creates an empty file using the current
    date and time as the filename. It then writes an empty 
    string to the file.

"""
filename = datetime.datetime.now()

def create_file():
    """This function creates a file"""
    with open(filename.strftime("%Y-%m-%d-%H-%M") + ".txt", "w") as file:
        file.write("") # Writing an empty string

create_file()
