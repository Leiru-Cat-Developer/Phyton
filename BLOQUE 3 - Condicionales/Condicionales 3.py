'''
    HACER UN PROGRAMA QUE PIDA 2 NUMEROS Y SE DE CUENTA CUAL DE ELLOS ES PAR Y CUAL IMPAR O
    SI AMBOS CUMPLEN UNA CONDICION
'''
numero1 = int(input("DIGITE EL PRIMER NUMERO: "))
numero2 = int(input("DIGITE EL SEGUNDO NUMERO: "))

if numero1%2 == 0 and numero2%2 == 0:
    print("AMBOS NUMEROS SON PARES")
elif numero1%2 == 0 and numero2%2 != 0:
    print(f"{numero1} ES PAR")
elif numero1%2 != 0 and numero2%2 == 0:
    print(f"{numero2} ES PAR")
else:
    print("AMBOS NUMEROS SON IMPARES")