# reading TXT file
'''file_path = "test.txt"
with open(file_path, "r") as file:
    content = file.read()
    print(content)'''

# reading JSON files
'''import json
file_path = "test.json"
with open(file_path, "r") as file:
    content = json.load(file)
    # print(content)        # prints the whole dictionary
    print(content["name"])  # prints corresponding value related to key'''

# reading CSV file    
import csv
file_path = "test.csv"
with open(file_path, 'r') as file:
    content = csv.reader(file)
    for row in content:
        # print(row)    # prints the whole 2d collection
        print(row[0])   # prints particular column acc to index
    