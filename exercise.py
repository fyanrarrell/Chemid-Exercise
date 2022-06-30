import csv
file = open("chemid-sample.csv")
filecontent = csv.reader(file)
for row in filecontent:
    print(row)