'''numero fuera de rango
escribe un programa que le pida un numero ,si el numero no esta en rango de 10 a 20 que le salga un 
error que le indique que esta fuera de rango'''

numero= int(input("ingrese un numero:"))

if not (10 <= numero <= 20):
    print("numero fuera de rango")
else:
    print("numeor dentro del rango")
