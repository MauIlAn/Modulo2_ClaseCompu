from pickle import TRUE

def lista():
  print("Introduce un valor para la creación de la lista")
  X = int(input())
  lst = list(range(1, X+1))
  def f(n):
      return all([not n%x==0 for x in range (2,n)])
      
  for i in range(1,X+1):
      primos = []
      for lNum in range(1, X+1):
          if (f(lNum)):
              primos.append(lNum)
  print("Lista generada con el valor asignado: " + str(lst))
  print("Lista de primos con ell valor asignaado: " + str(primos))
    
lista()
