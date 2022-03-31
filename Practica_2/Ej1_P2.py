with open("Readme.txt", "rt") as f:
    lineas = [linea for linea in f.readlines() if ("http" or "https") in linea]
    for i in lineas :
        print(i)