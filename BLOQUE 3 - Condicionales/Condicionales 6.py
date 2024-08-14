'''
    CONSTRUIR UN PROGRAMA QUE SIMULE EL FUNCIONAMIENTO DE UNA CALCULADORA QUE PUEDE REALIZAR
    LAS 4 OPERACIONES ARITMETICAS (SUMA, RESTA, MULTIPLICACION, DIVISION). EL USUARIO DEBE
    ESPECIFICAR LA OPERACION CON LA PRIMERA LETRA DE CADA OPERACION:

    S,s     SUMA
    R,r     RESTA
    M,m     MULTIPLICACION
    D,d     DIVISION
'''
numero1 = int(input("DIGITE EL NUMERO UNO: "))
numero2 = int(input("DIGITE EL NUMERO DOS: "))
opcion = input("DIGITE LA INICIAL DE LA OPERACION QUE DESEA: ")

if opcion == 'S' or opcion == 's':
    resultado = numero1+numero2
    print(f"EL RESULTADO DE LA SUMA ES: {resultado}")
elif opcion == 'R' or opcion == 'r':
    resultado = numero1-numero2
    print(f"EL RESULTADO DE LA RESTA ES: {resultado}")
elif opcion == 'M' or opcion == 'm':
    resultado = numero1*numero2
    print(f"EL RESULTADO DE LA MULTIPLICACION ES: {resultado}")
elif opcion == 'D' or opcion == 'd':
    resultado = numero1/numero2
    print(f"EL RESULTADO DE LA DIVISION ES: {resultado}")
else:
    print("DIGITE UNA OPCION VALIDA")