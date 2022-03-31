cadena = "seminario python primer semestre"
frase = cadena.split(' ')

letra = input("Ingresa una letra ")
if(letra).isalpha() :
    for i in frase :
        if i[0] == letra :
            print(i)
else :
    print('No has ingresado ninguna letra') 