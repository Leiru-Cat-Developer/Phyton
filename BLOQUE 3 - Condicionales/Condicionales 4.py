'''
    HACER UN PROGRAMA QUE PIDA 3 NUMEROS Y DETERMINE CUAL ES EL MAYOR
'''
numero1 = int(input("DIGITE EL PRIMER NUMERO: "))
numero2 = int(input("DIGITE EL SEGUNDO NUMERO: "))
numero3 = int(input("DIGITE EL TERCER NUMERO: "))

if numero3<numero2<numero1:
    print(f"{numero1} ES EL MAYOR")
elif numero1<numero3<numero2:
    print(f"{numero2} ES EL MAYOR")
elif numero1<numero2<numero3:
    print(f"{numero3} ES EL MAYOR")