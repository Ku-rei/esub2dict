# First check that the dictionary file is formatted as intended. Comment this section if file is heavy.

n = 0 # number of errors: lines without tab
t = 0 # number of errors: tabs with more than one tab character
z = 0 # tabs found with no errors


with open('notags.txt', 'r', encoding= 'utf-8') as file:  # Change name of file if necessary
    number_of_lines = 0
    for line in file:
        number_of_lines += 1
        tab_position = line.find('\t')
        if tab_position == -1:
            n+=1
        if line[tab_position + 1 :].find('\t') != -1:
            t += 1

        if tab_position != -1:
            z += 1

if n == 0:
    print('No lines without Tab')

if t == 0:
    print("No lines with more than one Tab")

if z == number_of_lines:
    print("All ok, the number of Tab chracters found is the same as the number of entries")

print(str(z))
print(str(number_of_lines))

# ----------------------------------------------------------------------------------
# Now, convert it into a CSV.

import csv

new_format = [] # needs to be a list of list, to convert it into a csv

with open('notags.txt', 'r', encoding='utf-8') as file:
    for line in file:
        tab_positio = line.find('\t')
        part1 = line[:tab_positio] # slice first part of the string/line, without tab
        part2 = line[tab_positio + 1 :] # slice the second part, without tab
        couple = [part1, part2] # list with the two parts == 1 entry
        new_format.append(couple) # add new entry to the list


new_file_name = 'dictionary.csv' # Change name of the file here

with open(new_file_name, 'w', encoding='utf-8', newline = '') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerows(new_format)

print(f"CSV file with the dictionary has been created with the name '{new_file_name}'")


