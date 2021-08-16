def sum(num1, num2):
    result= num1+num2
    return result

nume1=int(input("Ingrese un numero: "))
nume2=int(input("Ingrese otro numero: "))
total=sum(nume1, nume2)
print ("El total de la suma es: ", total)

def mult(num1, num2):
    result=num1*num2
    return result

nume3=int(input("Ingrese un tercer numero: "))
total2=mult(nume3,total)
print ("La multiplicacion de la suma con el tercer numero es: ", total2)
