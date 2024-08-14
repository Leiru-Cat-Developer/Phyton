'''
    HACER UN PROGRAMA QUE SIMULE UN CAJERO AUTOMATICO CON UN SALDO INICIAL DE $1,000 Y TENDRA EL
    SIGUIENTE MENU DE OPCIONES:

    1. INGRESAR DINERO
    2. RETIRAR DINERO
    3. DEPOSITAR DINERO
    4. SALIR
'''
saldoInicial = 1000

print("1. INGRESAR DINERO")
print("2. RETIRAR DINERO")
print("3. MOSTRAR DINERO")
print("4. SALIR")

opcion = int(input("DIGITE LA OPCION: "))

if opcion == 1:
    ingreso = float(input("DIGITE LA CANTIDAD QUE DESEA INGRESAR: $"))
    saldoInicial += ingreso
    print(f"SU SALDO AHORA ES DE: ${saldoInicial}")
elif opcion == 2:
    retiro = float(input("DIGITE LA CANTIDAD QUE DESEA RETIRAR: $"))
    if retiro > saldoInicial:
        print(f"NO SE PUEDE RETIRAR POR QUE SOLO HAY ${saldoInicial}")
    else:
        saldoInicial -= retiro
        print(f"SU SALDO AHORA ES DE: ${saldoInicial}")
elif opcion == 3:
    print(f"SU SALDO AHORA ES DE: ${saldoInicial}")
elif opcion == 4:
    print("S A L I E N D O . . .")
else:
    print("DIGITE UNA OPCION VALIDA")