import csv
import json

with open("students.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
rows = list(datos[0].keys())
#print(rows)

with open("students.csv", "w", newline="", encoding="utf-8") as archivo_csv:
    escritor = csv.DictWriter(archivo_csv, fieldnames= rows)
    print(escritor)
    escritor.writeheader()
    escritor.writerows(datos)
