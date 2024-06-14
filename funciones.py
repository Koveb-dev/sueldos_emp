import time
import os


def menu_app():
    print('\t   Menú\n\t1. Registra trabajador\n\t2. Lista trabajadores\n\t3. Imprimiir planilla de sueldos\n\t4. Salir')


def validar_opciones(p_opcs):
    while True:
        try:
            opc = int(input('\tIngrese una opción: '))
            if opc in p_opcs:
                return opc
            else:
                print(
                    'ERROR! debe ingresar una opción valida, opciones validas(1,2,3,4)!')
            time.sleep(1)
            os.system('cls')
        except:
            print('ERROR! debe ingresar números enteros!')


def nombre_trabajador():
    while True:
        nombre_trabj = str(input('Ingrese el nombre del trabajador: '))
        if len(nombre_trabj.strip()) >= 3:
            return nombre_trabj
        else:
            print('ERROR! el nombre del trabajador debe contener al menos 3 letras!')


def apellido_trabajador():
    while True:
        apellido_trabj = str(input('Ingrese el apellido del trabajador: '))
        if len(apellido_trabj.strip()) >= 3:
            return apellido_trabj
        else:
            print('ERROR! el apellido del trabajador debe contener al menos 3 letras!')


def cargo_trabajador(p_cargos):
    while True:
        try:
            cargo = int(
                input('Ingrese el cargo (1:CEO 2:Desarrollador 3:Analista): '))
            if cargo in p_cargos:
                return cargo
            else:
                print('ERROR! debe ingresar una opción valida, opciones valida(1,2,3)!')
            time.sleep(1)
            os.system('cls')
        except:
            print('ERROR! debe ingresar un número entero!')


def sueldo_bru_trabajador():
    while True:
        try:
            sueldo_bruto = int(input('Ingrese sueldo bruto del trabajador: '))
            if sueldo_bruto >= 600000 and sueldo_bruto <= 99999999:
                return sueldo_bruto
            else:
                print(
                    'ERROR! el sueldo bruto debe estar en un rango de $600.000 a $99.999.999!')
            time.sleep(1)
            os.system('cls')
        except:
            print('ERROR! debe ingresar números enteros!')


def salida_app():
    for i in range(1, 4):
        print('Saliendo de la sueldos emp', ("."*i))
        time.sleep(1)
        os.system('cls')


def crear_archivotxt():
    with open("sueldos_emps.txt", "w", newline="") as archivo:
        archivo.write
