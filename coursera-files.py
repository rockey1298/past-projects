import os


def new_directory(directory, filename):
    mylist = []
    # Before creating a new directory, check to see if it already exists
    if os.path.isdir(directory) == True:
        with open(directory, "x"):
            # Create the new file inside of the new directory
            os.chdir(directory)
    else:
        if os.path.isdir(filename) == True:
            with open(filename, "x"):
                for fn in directory:
                    mylist = mylist.append(fn)
            # Return the list of files in the new directory
            return mylist


print(new_directory("PythonPrograms", "script.py"))
