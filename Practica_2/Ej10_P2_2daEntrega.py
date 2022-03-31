archNombres = open("nombres.txt", "r", encoding="utf-8")
archEval1 = open("eval1.txt", "r", encoding="utf-8")
archEval2 = open("eval2.txt", "r", encoding="utf-8")

nombres = archNombres.read().split()
eval1 = archEval1.read().split(",")
eval2 = archEval2.read().split(",")

archNombres.close()
archEval1.close()
archEval2.close()

alumnos = []
suma = 0
for nombre, val1, val2 in zip(nombres, eval1, eval2) :
    alumnos.append((nombre, int(val1) + int(val2)))
    suma += int(val1) + int(val2)

print(f"Promedio {suma / len(alumnos):.2f}")

for alum in alumnos :
    if alum[1] < suma / len(alumnos) :
        print(alum[0], alum[1])