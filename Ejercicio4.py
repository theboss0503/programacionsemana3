print ("Inicio de Sesion")
print("Ingrese las credenciales correspondientes")
user=str(input("Ingrese su usario: "))
password=str(input("Ingrese su contraseña: "))

if user and password == "UGB":
     print ("Ha ingresado correctamente al sistema")
else:
    print ("Credenciales incorrectas")
    