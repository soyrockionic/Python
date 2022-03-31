nombresuno = ['Andres', 'Ariana', 'Sofia', 'David', 'Damian', 'Raul', 'Franco', 'Manuel', 'Agustin', 'Juan']

nombresdos = ['Agustin', 'Ailen', 'Alfredo', 'Amalia', 'Ariana', 'Juan', 'Franco', 'Braian', 'Carla', 'Diego']

eval1 = [81, 60, 72, 24, 15, 80, 91, 12, 70, 29]

eval2 = [30, 95, 28, 84, 84, 75, 43, 66, 51, 4]

#for val1, val2, val3 in zip(nombres, eval1, eval2) :
    #print(val1, val2, val3)

#print()
#for i in range(len(nombres)) :
    #print(f"{i} {nombres[i]} {eval1[i]} {eval2[i]}")

print()
nombresEnAmbos = []
for n in nombresuno :
    if n in nombresdos :
        nombresEnAmbos.append(n)    
print(nombresEnAmbos)


print()
print('   {:<10}  {:>8} {:>8} {:>8}'.format('Nombre', 'Eval1', 'Eval2', 'Total'))
for i, valor in enumerate(zip(nombresuno, eval1, eval2)) :
    print('{:>2} {:<15} {:<8} {:<8} {:<8}'.format(i, valor[0], valor[1], valor[2], valor[1] + valor[2]))