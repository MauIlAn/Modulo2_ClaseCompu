#First program "hello world"
numero = int(input('Ingrese un numero mayor a 1: '))
def es_primo(numero):
contador = 0
for i in range(1,numero):
if i == 1 or i == numero:
continue
if numero % i == 0:
contador += 1
if contador == 0:
print(“Si es número primo”)
else:
print(“No es número primo”)
es_primo(numero)
