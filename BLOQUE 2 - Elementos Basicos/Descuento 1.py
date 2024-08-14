'''
    UNA TIENDA OFRECE UN DESCUENTO DEL 15% SOBRE EL TOTAL DE LA COMPRA Y UN CLIENTE DEBERA SABER
    CUANTO DEBERA PAGAR FINALMENTE POR SU COMPRA
'''
precio = float(input("DIGITE EL PRECIO DE LA COMPRA: "))

descuento = precio * 0.15
precioConDescuento = precio - descuento


print(f"\nEL PRECIO TOTAL A PAGAR ES: {precioConDescuento:.2f}")
print(f"\nEL DESCUENTO ES: {descuento:.2f}")