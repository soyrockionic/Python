import csv
import os

ruta = os.path.join(os.getcwd(), "netflix_titles.csv")

archivo = open(ruta, "r", encoding='utf-8')
data_net = csv.reader(archivo, delimiter=',')

datos = next(data_net)
print(f"{datos[5]:<20} {datos[1]}\n"+"-"*30)

for linea in data_net:
    if linea[5] == "United States" :
        print(f"{linea[5]:<20} {linea[1]}")
