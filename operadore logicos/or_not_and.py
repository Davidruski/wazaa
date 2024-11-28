'''escribe un progama que le pida al usuario nombre y contraseña el cual indique si la contraseña es correcta o incorrecta'''

usuario= input("ingreas el nombre del usuario")
contraseña= input("ingresa la contraseña")

if usuario == "admin" and contraseña == "12345":
    print("acceso permitido")
else:
    print("acceso denegado")
