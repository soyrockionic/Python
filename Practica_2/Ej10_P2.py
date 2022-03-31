nombresuno = ['Andres', 'Ariana', 'Sofia', 'David', 'Damian', 'Raul', 'Franco', 'Manuel', 'Agustin', 'Juan']

eval1 = [81, 60, 72, 24, 15, 80, 91, 12, 70, 29]

eval2 = [30, 95, 28, 84, 84, 75, 43, 66, 51, 4]

def calcular_promedio(dicci) :
    suma = 0
    for i in dicci :
        suma += dicci[i]
    promedio = 0 if len(dicci) == 0 else suma / len(dicci)
    return promedio

def menores_al_prom(dicci) :
    print('------------------')
    for i in dicci :
        if dicci[i] < calcular_promedio(dicci) :
            print(i)

print()
dicci = {}
for i in range(len(nombresuno)) :
    dicci[nombresuno[i]] = eval1[i] + eval2[i]

for i in dicci :
    print(i + f" {dicci[i]}")

print()
print(f"Promedio {calcular_promedio(dicci):.2f}")

menores_al_prom(dicci)