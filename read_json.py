import json
#Rename in students.json for name of your file
with open("students.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

for i in datos:
    print(i['nombre'],'-',i['nota'])
