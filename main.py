import random

numero= random.randint(0,100)
MIN=0
MAX=99
def introducir_numero(invite):
  while True:
    print(invite, end=":")
    dato_introducido=input()
    try:
      dato_introducido=int(dato_introducido)
    except:
      print("Solo están autorizados los caracteres de [0-9]:",file=sys.stderr)
  else:
    return dato_introducido
      
    
def introducir_numero_extremo(invite,minimo=MIN,maximo=MAX):
  while True:
    invite="{} entre {} y {} incluidos".format(invite,minimo,maximo) 
    dato_introducido= introducir_numero(invite)
    if minimo<=dato_introducido<=maximo:
      break
  return dato_introducido

def jugar_partida(numero, minimo,maximo):
  intento= introducir_numero_extremo("Adivine el número",minimo,maximo)
  if intento<numero:
    print("Demasido pequeño.")
    minimo=intento+1
    victoria= False
  elif intento>numero:
    print("Demasiado grande.")
    maximo=intento-1
    victoria= False
  else:
    print("Ha ganado")
    victoria=True
    minimo=maximo=intento
  return victoria, minimo,maximo

def extremo():
  while True:
    minimo=introducir_numero("Selecciona el mínimo ")
    maximo=introducir_numero("Selecciona el máximo ")
    if maximo>minimo:
      return    minimo,maximo
def pedir_numero_incognita():
  return introducir_numero_extremo("Introduce el número a adivinar",minimo,maximo)      
def jugar_una_partida(numero,minimo,maximo):
    while True:
      victoria,minimo,maximo=jugar_partida(numero,minimo,maximo)
      if victoria:
        return


def jugar():
  minimo,maximo=extremo()
  numero=pedir_numero_incognita()
  jugar_una_partida(numero,minimo,maximo)


if __name__=='__main__':
  print("El módulo se ejecuta")
  jugar()
else:
  print("El módulo se ha importado")