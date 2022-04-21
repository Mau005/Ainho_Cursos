from random import randint
numeros_aleatorios = [randint(1,200) for _ in range(200)]
Numeros_impar = []
Numeros_par = []

for numeros in numeros_aleatorios:
    if numeros % 2 == 0:
        Numeros_par.append(numeros)
    else:
        Numeros_impar.append(numeros)

print()
print(f"Numeros Impar: {Numeros_impar}")
print()
print(f"Numeros Par: {Numeros_par}")