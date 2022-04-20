#numeros Impares
import random
lista_impar = []
lista_par = []


for numeros in range(0,200):
    numero_generado = random.randint(0,200)
    if numero_generado % 2 == 0:
        lista_par.append(numero_generado)
    else:
        lista_impar.append(numero_generado)


print(f"Lista Impar: {lista_impar}")
print(f"Lista Par: {lista_par}")
