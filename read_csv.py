import csv
with open("prueba.csv", "r", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
