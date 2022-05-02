import csv
import os

ruta = os.path.join(os.getcwd(), "netflix_titles.csv")

archivo = open(ruta, "r", errors="ignore")
data_net = csv.reader(archivo, delimiter=',')

datos = next(data_net)
print(f"{datos[2]}\n"+"-"*50)


def shows(a,i):
    if a in i[6]:
        print(i[2])

a = "2021"
for i in data_net:
    shows(a,i)