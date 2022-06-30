import csv
file = open("chemid-sample.csv")
filecontent = csv.reader(file)
for row in filecontent:
    # print(row[5])

    a_string=row[5]
    for character in '([=#)]':
        a_string = a_string.replace(character, '')
    print(a_string)