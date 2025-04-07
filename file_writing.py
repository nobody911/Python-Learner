# WRITING FILES

# TXT FILES 
# file_data = "I like momos"
'''file_data = ["oggy", "jarvis", "jack", "bob", "olivia"]
file_path = "test.txt"

try:
    with open(file_path, 'w') as file:
        for i in file_data:
            file.write(i + "\n")
        print(f"A text file at '{file_path}' has been written")
except FileExistsError:
    print("The given file already exists....")'''

# JSON FILES (deals with key:value pairs)

'''import json
file_path = "test.json"
file_data = {"name": "Oggy",
             "age": 22,
             "job": "work from home"}
try:             
    with open(file_path, "w") as file:
        json.dump(file_data, file, indent=4)
        print(f"A json file at '{file_path}' was written")
except Exception:
    print("Something wrong happened....!!!")    '''

# CSV FILES (deals with spreadsheet data)

import csv
file_path = "test.csv"
file_data = [["Name", "Age", "Job"],
             ["Oggy", 30, "Housemaid"],
             ["Jack", 35, "Soldier"],
             ["Bob", 40, "Boxer"]]
with open(file_path, "w") as file:
    writer = csv.writer(file)
    for rows in file_data:
        writer.writerow(rows)
    print(f"A csv file at '{file_path}' was written")