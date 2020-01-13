import os

"""
Goes through file in specific folder and then gets all data and saves them in one file
"""

# path = 'd:\\SIBA\\Scripty\\Projekt\\msk\\data\\'
path = input("Zadej cestu k souborum \n")

list_of_files = os.listdir(path)
file_to_write = 'complete_data.txt'

print(len(list_of_files))

current_file = 0

complete_data = ''

for file in list_of_files:
    with open(path + file, encoding='ANSI') as org_file:
        lines_from_file = org_file.readlines()
        for line in lines_from_file:
            complete_data += line
        current_file += 1

with open(path + file_to_write, 'w', encoding='UTF-8') as file:
    file.write(complete_data)

pass
