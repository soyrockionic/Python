from collections import Counter

frase = input("ingrese una frase: ").lower()
pal = input("ingrese una palabra: ").lower()

print(f"{pal} esta {Counter(frase.split())[pal]} veces en la frase")