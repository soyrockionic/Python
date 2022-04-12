import random
numero_aleatorio = random.randrange(101)
gane = False
print("Tenés 5 intentos para adivinar un entre 1 y 100")
intento = 1
while intento <= 5 and not gane:
    numero_ingresado = int(input('Ingresa tu número: '))
    if numero_ingresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intentos!!!'.format(intento))
        gane = True
    else:
        print('Fallaste ... No.. ese número no es... Seguí intentando.')
        intento += 1
if not gane:
    print('\n Perdiste :(\n El número era: {}'.format(numero_aleatorio))
