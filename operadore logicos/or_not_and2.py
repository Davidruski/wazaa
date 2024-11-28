'''escribe un programa el cual le pida al usuario la edad y le permita introducirla,indique cual es su edad
so ña edad esta entre los 18 y 30 años
edad mayor o igual a 65
si cumple con las condiciones print acceso permitido
en caso contrario print acceso denegado'''

edad= int(input("ingrese su edad"))

if (18<= edad<= 30) or edad >= 65:
    print("acceso permitido al evento")
else:
    print("acceso denegado")
