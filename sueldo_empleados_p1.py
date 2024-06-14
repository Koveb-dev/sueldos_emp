import time
import os
from funciones import *

trabajador = []
trabajadores = []


print('Bienvenido a la app de sueldos emp!')
time.sleep(1)
os.system('cls')
opciones = (1, 2, 3, 4)
cargos = ("CEO", "Desarrollador", "Analista")

while True:
    menu_app()
    op = validar_opciones((opciones))

    if op == 1:
        print('Registrar trabajador!')
        time.sleep(1)
        os.system('cls')
        nombre_trabj = nombre_trabajador()
        apellido_trabj = apellido_trabajador()
        nom_trabajador = str(nombre_trabj + " " + apellido_trabj)
        tipo_cargo_trabj = cargo_trabajador((1, 2, 3))
        if tipo_cargo_trabj == 1:
            tipo_cargo_trabj = cargos[tipo_cargo_trabj-1]
        elif tipo_cargo_trabj == 2:
            tipo_cargo_trabj = cargos[tipo_cargo_trabj-1]
        else:
            tipo_cargo_trabj = cargos[tipo_cargo_trabj-1]
        sueldo_bruto = sueldo_bru_trabajador()
        desc_salud = round(sueldo_bruto * 0.07,)
        desc_afp = round(sueldo_bruto * 0.12,)
        sueldo_liq = round(sueldo_bruto - (desc_afp+desc_salud),)

        trabajador = [nom_trabajador, tipo_cargo_trabj,
                      sueldo_bruto, desc_salud, desc_afp, sueldo_liq]
        trabajadores.append(trabajador)
        print('TRABAJADOR AGREGADO!')
        time.sleep(1)
        os.system('cls')

    elif op == 2:
        if len(trabajadores) >= 1:
            while True:
                for i in trabajadores:
                    print(
                        "Trabajador\t Cargo\t Sueldo Bruto\t Desc.Salud\t Desc.AFP\t Liquido a pagar")
                    print(f"{i}\t", sep="      ")

                mensaje = str(
                    input('¿Deseas salir? Ingrese ("S": salir)("N":Redirigir a lista): '))
                if mensaje.upper() in ("S", "N"):
                    if mensaje == "S":
                        print('Saliendo.')
                        time.sleep(1)
                        os.system('cls')
                        break
                    else:
                        print('Redirigiendo.')
                    time.sleep(1)
                    os.system('cls')
                else:
                    print(
                        'ERROR! debe ingresar una opción valida,opciones validas ("S" o "N")!')
        else:
            print('NO HAY REGISTRO DE TRABAJADORES!')
    elif op == 3:
        with open("sueldos_emps.txt", "w+", newline="") as archivo:

        while True:
            for i in trabajadores:
                print(
                    "Trabajador\t Cargo\t Sueldo Bruto\t Desc.Salud\t Desc.AFP\t Liquido a pagar")
                print(f"{i}\t", sep="      ")

    else:
        if op == 4:
            salida_app()
            break
