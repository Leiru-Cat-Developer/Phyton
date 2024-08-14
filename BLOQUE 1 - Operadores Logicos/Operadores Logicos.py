'''
    PERMITE CONSTRUIR EXPRECIONES LOGICAS, SE OBTIENE COMO RESULTADO BOOL

    AND         - AND
    OR          - OR
    NEGACION    - NOT

    TABLA DEL OPERADOR AND (MULTIPLICACION)

    TRUE    AND     TRUE    =   TRUE
    TRUE    AND     FALSE   =   FALSE
    FALSE   AND     TRUE    =   FALSE
    FALSE   AND     FALSE   =   FALSE




    TABLA DEL OPERADOR OR (SUMA)

    TRUE    AND     TRUE    =   TRUE
    TRUE    AND     FALSE   =   TRUE
    FALSE   AND     TRUE    =   TRUE
    FALSE   AND     FALSE   =   FALSE



    TABLA DEL OPERADOR NOT (CONTRARIO)

    NOT TRUE     = FALSE
    NOT FALSE    = TRUE

    PRIORIDAD DE LOS OPERADORES LOGICOS:

    1. NOT
    2. AND
    3. OR
'''
a = 10
b = 12
c = 13
d = 10

resultado = not((a>b)or(a<c)and(a==c)or(a>=b))

print(resultado)