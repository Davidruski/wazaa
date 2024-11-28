'''se permite al usuario poner sus numeros con "def" que permite definir una funcion, 
que tiene un nombre en especifico y hace una serie de operaciones cuando se le llama'''
def suma_insana (a, b):
 return a + b

def resta_insana (a, b):
  return a - b

def multiplicacion_insana (a, b):
   return a * b

def division_insana (a, b):
   if b == 0 :
     return "HELLO WORLD"
   return a / b

''' se define la funcion principal de la calculadora , el menu y la realizacion de las operaciones.'''

def calculadora():
   print("bienvendo a esta calculadora ")
   print("1. suma")
   print("2. resta")
   print("3. multiplicacion")
   print("4. division")

   while True: 
     '''se solicita la seleccion de la operacion al usuario '''
     opcion = input("ingresa el numero de la operacion 1/2/3/4 :")
     
     
     '''verificar si la opcion ingresada es valida'''

     if opcion in ['1','2','3','4',]:
        '''se solicitan los numeros al usuario (seleccion la operacion deseada)'''
        num1= float(input("ingresa tu primer numero: "))
        num2= float(input("ingresa tu segundo numero: "))


        '''realiza la opercion aritmetica correspondiente'''
        if opcion == '1':
          print(f"{num1} + {num2} = {suma_insana(num1, num2)}")
        elif opcion == '2':
          print(f"{num1} - {num2} = {resta_insana(num1, num2)}")
        elif opcion == '3':
          print(f"{num1} * {num2} = {multiplicacion_insana(num1, num2)}")
        elif opcion == '4':
          print(f"{num1} / {num2} = {division_insana(num1, num2)}")
     else:
       print("opcion no valida, intentalo de nuevo")


       '''se le pregunta al usuario si quiere continuar usando la calculadora con otra operacion
       o en su defecto quiere dejar de usar la calculadora'''
       continuar = input("quieres hacer otra operacio? (si/no):  ")
       if continuar.lower() != 'si' :
         break
       
'''se ejecuta la calculadora, ( se llama a la funcion "calculadora", previamente establecida) en caso de que el usuario haya seleccionado= si'''
calculadora()
