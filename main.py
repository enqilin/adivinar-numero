import random

numero= random.randint(0,100)
contador=0

print(numero)
n=int(input("Dime el número que es entre 1-99: "))


while n!=numero:
  if n<numero:
    n=int(input("El número es menor, dime de nuevo el número: "))
  else:
    n=int(input("El número es  mayor, dime de nuevo el número: "))
    contador+=1
print("Has adivinado el número")
#