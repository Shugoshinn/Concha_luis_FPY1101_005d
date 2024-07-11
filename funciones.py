import random
import os, time, csv, msvcrt

aleatorio = random.randint(300000, 2500000)
sueldos = []
total_empleados = []
total_sueldo = []
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def asignar_sueldos_alea():
    for x in (11):
        random.randint(trabajadores)
        sueldos.append(trabajadores)

def clasificar_sueldos():
    if sueldos < 800000:
        print("Sueldos menores a $800000","TOTAL: ",total_empleados )
        print("Nombre empelado",               "Sueldo")
        print(trabajadores,                     sueldos)
        print(trabajadores,                     sueldos)
    else: 
        print("ERROR! NO SE ENCONTRARON REGISTROS DE SUELDO")

    if sueldos >= 800000 and sueldos <= 2000000:
        print("Sueldos entre $800000","y 2000000","TOTAL: ",total_empleados )
        print("Nombre empelado",               "Sueldo")
        print(trabajadores,                     sueldos)
        print(trabajadores,                     sueldos)
    else:
        print("ERROR! NO SE ENCONTRARON REGISTROS DE SUELDO")

    if sueldos > 2000000:
        print("Sueldos superiores a","$2000000","TOTAL: ",total_empleados )
        print("Nombre empelado",               "Sueldo")
        print(trabajadores,                     sueldos)
        print(trabajadores,                     sueldos)  
    else:
        print("ERROR! NO SE ENCONTRARON REGISTROS DE SUELDO")

    print("TOTAL SUELDOS: ",total_sueldo= sueldos + sueldos +sueldos)  
    

def ver_estadisticas():
    print(sueldos.extend())
    print(sueldos.index())
    print (sueldos+trabajadores)

def reporte_sueldos():
    with open ("x", newline= ".csv")as archivo:
        escritor = archivo
    print("Nombre empleado",           "Sueldo Base",            "Descuento Salud",            "Deescuento AFP",             "Sueldo líquido")
    print(trabajadores,                  sueldos,                   sueldos*0.7,                sueldos*0.12,                 sueldos-sueldos*0.7-sueldos*0.12)
    print(trabajadores,                  sueldos,                   sueldos*0.7,                sueldos*0.12,                 sueldos-sueldos*0.7-sueldos*0.12)  

def salir():
    print("Finalizando programa...")
    print("Desarrollado por Luis Concha")
    print("RUT 21.653.367-4")
    exit()
