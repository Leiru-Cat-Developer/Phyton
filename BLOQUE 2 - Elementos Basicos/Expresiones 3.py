'''
    HACER UN PROGRAMA PARA INGRESAR EL RADIO DE UN CIRCULO Y SE REPORTE SU AREA Y LA LONGITUD
    DE LA CIRCUNFERENCIA CON LAS 2 SIGUIENTES FORMULAS:

        - area = pi * radio**2
        - longitud = 2 * radio * pi
'''

#IMPORTAMOS EL MODULO MATH PARA PODER UTILIZAR EL VALOR DE PI
import math
radio = float(input("DIGITE EL VALOR DEL RADIO: "))
area = math.pi * radio**2
longitud = 2 * radio * math.pi

print(f"\nEL AREA DEL CIRCULO ES: {area:.2f}")          #VALOR REDONDEADO
print(f"LA LONGITUD DEL CIRCULO ES: {longitud:.2f}")    #VALOR REDONDEADO