import csv
file = open("chemid-sample.csv")
filecontent = csv.reader(file)
output = open("output.csv", 'w')
writer = csv.writer(output)

for row in filecontent:
    print(row[5])

    trimmed_SMILE=row[5]
    for character in '([=#)]':
        trimmed_SMILE =  trimmed_SMILE.replace(character, '')
    print(trimmed_SMILE)
    if (trimmed_SMILE.__contains__("C1CCCCC1")):
        print(row)
        writer.writerow(row)

        

