#LISTAS
lista = ["LUNES","MARTES","MIERCOLES","JUEVES","VIERNES",40,17.77,[3,4,5],True]

print(lista[0])         #EMPIEZA A CONTABILIZAR DESDE LA DERECHA
print(lista[-1])        #EMPIEZA A CONTABILIZAR DESDE LA IZQUIERDA
print(lista[0:3])       #IMPRIME LOS ELEMENTOS ENTRE EL 0 Y 3
print(lista[:5])        #IMPRIME TODOS LOS VALORES DESDE EL INICIO HASTA EL 5
print(lista[0:])        #IMPRIME TODOS LOS VALORES DESDE 0 HASTA EL FINAL
print(len(lista))       #NUMERO DE ELEMENTOS AGREGADOS A LA LISTA

lista.append("URIEL")              #SE AGREGAN  DATOS EN LA POCISION FINAL
lista.append(6)                    #SE AGREGAN DATOS EN LA POCISION FINAL
lista.insert(2,3)   #SE AGREGAN DATOS EN POCISIONES ESPECIFICAS
lista.extend([8.9,10])              #AGREGAR MUCHOS DATOS EN UN SOLO COMANDO

print(lista)

print(3 in lista)                   #PREGUNTAMOS SI ES QUE UN DATO SE ENCUENTRA EN LISTA (TRUE/FALSE)
print(lista.index(40))              #RETORNA LA POCISION DEL ELEMENTO QUE ESTAMOS BUSCANDO
print(lista.count(17.77))           #BUSCA CUANTAS VECES ES QUE SE REPITE UN DATO EN LA LISTA

lista.pop()                         #ELIMINA EL ULTIMO ELEMENTO DE LA LISTA
lista.pop(0)                        #ELIMINA UNA POCISION ESPECIFICA DE LA LISTA
lista.remove(40)                    #ELIMINA UN DATO DE UN VALOR ESPECIFICO EN LA LISTA
lista.clear()                       #ELIMINA TODO

print(lista)