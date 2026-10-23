import csv
with open("prueba.csv", "r", newline='') as file:#In "prueba.csv" you will be change for name of your archive
    reader = csv.reader(file)
    for row in reader:
        print(row)
