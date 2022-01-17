# 1. Cuenta regresiva: 
def countdown(num):
    lista = []
    for i in range(num, -1, -1):
        lista.append(i)
    return lista

resultado = countdown(5)
print(resultado)


# 2. Imprimir y devolver:
def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]

resultado = imprimir_y_devolver([1, 2])
print(resultado)


# 3. Primero más longitud:
def primero_mas_longitud(lista):
    return lista[0] + len(lista)

resultado = primero_mas_longitud([1, 2, 3, 4, 5])
print(resultado)


# 4. Valores mayores que el segundo:
def valores_mayores_que_el_segundo(lista):
    count = 0
    lista_nueva = []
    if len(lista) < 2:
        return False
    for i in lista:
        if i > lista[1]:
            count += 1
            lista_nueva.append(i)
    print(count)
    return lista_nueva

resultado = valores_mayores_que_el_segundo([5, 2, 3, 2, 1, 4])
print(resultado)
resultado2 = valores_mayores_que_el_segundo([3])
print(resultado2)


# 5. Esta longitud, ese valor:
def length_and_value(tamaño, valor):
    lista = []
    for i in range(0, tamaño):
        lista.append(valor)
    return lista

resultado = length_and_value(4, 7)
print(resultado)
resultado2 = length_and_value(6, 2)
print(resultado2)