# TAREA 1 Angel Pluas


#funcion para ingreso de dolares
def cantidad():
    global dolares
    dolares = int(input("Cuantos dolares tiene: "))

#constantes
ARS = 202.91
COL = 4849.99
MEX = 18.74


#inicio del programa
nombre = input("Cual es su nombre: ")

print(f"Hola {nombre}, Bienvenido al conversor de monedas")

print("Seleccione una de las siguiente opciones de conversion")

print("1 - Dolares estadounidenses a pesos argentinos")
print("2 - Dolares estadounidenses a pesos colombianos")
print("3 - Dolares estadounidenses a pesos mexicanos")

opcion = int(input("Seleccione la opcion: "))

if opcion ==1:
    cantidad()
    pesos = dolares * ARS
    print(f"Tienes {pesos} pesos argentions")
else:
    if opcion == 2:
        cantidad()
        pesos = dolares * COL
        print(f"Tienes {pesos} pesos colombianos")
    else:
        if opcion == 3:
            cantidad()
            pesos = dolares * MEX
            print(f"Tienes {pesos} pesos mexicanos")
        else:
            print("Seleccione una opcion correcta")