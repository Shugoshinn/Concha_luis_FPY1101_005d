import os, time
 
from funciones import *

while True:
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    opc = input("Ingrese opción: ")
    os.system('cls')
    if opc == '1':
        asignar_sueldos_alea()
    elif opc == '2':
        clasificar_sueldos()
    elif opc == '3':
        ver_estadisticas()
    elif opc == '4':
        reporte_sueldos()
    else:
        salir()
