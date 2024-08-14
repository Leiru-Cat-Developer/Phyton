#CONDICIONALES COMBINADOS
edad = int(input("DIGITE SU EDAD: "))

if 0 < edad < 120:
    print("EDAD CORRECTA")
    if edad >= 18:
        print("LA PERSONA ES MAYOR DE EDAD")
    else:
        print("LA PERSONA ES MENOR DE EDAD")
else:
    print("DIGITE UNA EDAD CORRECTA")