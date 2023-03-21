# TAREA 1.2 Angel Pluas

ARG=203.35
MXN=18.49
COL=4849.99

#funcion para convertir de dolares
def convertir_moneda(moneda,pais):
    cantidad_dolar = int(input("Ingrese la cantidad en Dolares : "))
    conversion=cantidad_dolar*moneda
    print(f" El valor es {conversion} pesos {pais}")

nombre = input("cual es su nombre: ")
print (f"Hola {nombre},bienvenidos al conversor de monedas ")
print ("Seleccione una conversion: ")
print ("1.- Pesos Argentinos")
print ("2.- Pesos Colombianos")
print ("3.- Pesos Mexicanos")
opcion = int(input("Seleccione la opcion "))

if opcion != 1 or opcion != 2 or opcion != 3:
    print("Ingrese un valor valido")
if opcion == 1 :
    convertir_moneda(ARG,"Argentinos")
if opcion == 2 :
    convertir_moneda(COL, "Colombianos")
if opcion == 3 :
    convertir_moneda(MXN, "Mexicanos")
