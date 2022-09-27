#Ejercicio de arreglos de un número tal hasta número n,programa Python para crear una cadena que consista en los enteros no negativos hasta n, igual para verificar número primos

def Conteo():
    lst = [i for i in range(1,int(Num)+1)]
    print(lst)
    
def numeros_primos():
    primos=[]
    for Num in lst:
        if numeros_primos():
            primos.append(Num)
    if primos:
        print("Los numeros primos son: ", primos)
    
    else:
        print("Ningún número ingresado es un número primo")  

print("¿Hasta que valor quieres contar?")
Num = input()
Conteo()
numeros_primos()
