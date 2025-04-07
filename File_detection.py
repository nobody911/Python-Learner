import os
path = "/mnt/c/Dark_Rituals/python/"
if os.path.exists(path):
    print(f"The file '{path}' exists")
    if os.path.isfile(path):
        print("It is a file")
    if os.path.isdir(path):
        print("It is a directory")
else:
    print("The location does not exist")