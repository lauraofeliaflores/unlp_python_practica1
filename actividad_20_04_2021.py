import csv
import requests
archivo = open("C:/Proyectos/proyectosPython/archivosPY/appstore_games.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')
items = list(csvreader)

for elem in items:
  if "ES" in elem[12]  and elem[7] == "0":
    print(elem[2])

def tryconvert(value, default, *types):
    for t in types:
        try:
            return t(value)
        except (ValueError, TypeError):
            continue
    return default

items.sort(reverse=True, key=lambda elem: tryconvert(elem[6], 0, int))

for x in range(0,9):
  print(items[x][4])
  icono = requests.get(items[x][4])
  juego = items[x][1]
  with open(f'C:/Proyectos/proyectosPython/archivosPY/ejemplo/clase6/{juego}.jpg', 'wb') as f:
    f.write(icono.content)
