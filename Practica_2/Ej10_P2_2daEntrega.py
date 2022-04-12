arch_nombres = open("nombres.txt", "r", encoding="utf-8")
arch_eval1 = open("eval1.txt", "r", encoding="utf-8")
arch_eval2 = open("eval2.txt", "r", encoding="utf-8")

nombres = arch_nombres.read().split()
eval1 = arch_eval1.read().split(",")
eval2 = arch_eval2.read().split(",")

arch_nombres.close()
arch_eval1.close()
arch_eval2.close()

alumnos = []
suma = 0
for nombre, val1, val2 in zip(nombres, eval1, eval2) :
    alumnos.append((nombre, int(val1) + int(val2)))
    suma += int(val1) + int(val2)

print(f"Promedio {suma / len(alumnos):.2f}")

for alum in alumnos :
    if alum[1] < suma / len(alumnos) :
        print(alum[0], alum[1])