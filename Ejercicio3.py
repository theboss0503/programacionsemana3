def conver(grados):
    result = (5/9) * (grados-32)
    return result

print ("CONVERTIDOR DE GRADOS FAHRENHEIT A CELSIUS")
gradosF=float(input("Ingrese los grados Fahrenheit que desea convertir: "))
gradosC=conver(gradosF)
print (gradosF,"grados Fahrenheit equvalen a ", gradosC, "grados Celsius")
