def es_anagrama():
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    print("¿Es anagrama?", sorted(palabra1.lower()) == sorted(palabra2.lower()))

def invertir_cadena():
    cadena = input("Ingrese una cadena para invertir: ")
    print("Resultado:", cadena[::-1])

def fibonacci():
    n = int(input("Ingrese un número para la secuencia de Fibonacci: "))
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    print("Fibonacci:", a)

def eliminar_duplicados():
    lista = input("Ingrese números separados por espacio: ").split()
    print("Lista sin duplicados:", list(set(lista)))

def es_palindromo():
    cadena = input("Ingrese una palabra o frase: ").replace(" ", "").lower()
    print("¿Es palíndromo?", cadena == cadena[::-1])

def contar_palabras():
    texto = input("Ingrese un texto: ").lower()
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    print("Frecuencia de palabras:", conteo)

def encontrar_mayor():
    lista = list(map(int, input("Ingrese números separados por espacio: ").split()))
    print("Número mayor:", max(lista))

def invertir_lista():
    lista = input("Ingrese elementos separados por espacio: ").split()
    print("Lista invertida:", lista[::-1])

def filtrar_pares():
    lista = list(map(int, input("Ingrese números separados por espacio: ").split()))
    print("Números pares:", [num for num in lista if num % 2 == 0])

def encontrar_segundo_mayor():
    lista = list(map(int, input("Ingrese números separados por espacio: ").split()))
    lista = list(set(lista))  # Eliminar duplicados
    if len(lista) < 2:
        print("No hay suficientes números para encontrar el segundo mayor.")
    else:
        lista.sort(reverse=True)
        print("Segundo mayor:", lista[1])

def contar_vocales():
    texto = input("Ingrese un texto: ").lower()
    vocales = "aeiou"
    print("Cantidad de vocales:", sum(1 for letra in texto if letra in vocales))

def ordenar_tuplas(lista_tuplas):
    return sorted(lista_tuplas, key=lambda x: x[1])

def ordenar_tuplas():
    tuplas = []
    n = int(input("Ingrese la cantidad de tuplas: "))
    for _ in range(n):
        elemento = input("Ingrese una tupla (ejemplo: 3,2): ")
        tuplas.append(tuple(map(int, elemento.split(','))))
    print("Lista ordenada:", sorted(tuplas, key=lambda x: x[1]))

def contar_unicos():
    cadena = input("Ingrese una cadena: ")
    print("Caracteres únicos:", len(set(cadena)))


def palabras_mas_largas():
    texto = input("Ingrese un texto: ")
    n = int(input("¿Cuántas palabras más largas desea ver?: "))
    palabras = texto.split()
    palabras.sort(key=len, reverse=True)
    print(f"Las {n} palabras más largas:", palabras[:n])


def es_primo():
    n = int(input("Ingrese un número para verificar si es primo: "))  # Pide el número al usuario
    if n < 2:
        print(f"{n} no es primo.")
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} no es primo.")
            return False
    print(f"{n} es primo.")
    return True


def menu():
    while True:
        print("\nMenu de opciones")
        print("1. Anagrama")
        print("2. Invertir Cadena")
        print("3. Fibonaci")
        print("4. Eliminar duplicados")
        print("5. Palindromo")
        print("6. Contar palabras")
        print("7. Encontrar mayor elemento")
        print("8. Invertir lista")
        print("9. Filtrar pares")
        print("10. Encontrar el segundo mayor")
        print("11. Contar vocales")
        print("12. Ordenar lista de Tuplas")
        print("13. Cotar caracteres unicos")
        print("14. Enconttrar palabra mas larga")
        print("15. encontrar numeros primos")
        print("S. Salir  ")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            es_anagrama()
        elif opcion == "2":
            invertir_cadena()
        elif opcion == "3":
            fibonacci()
        elif opcion == "4":
            eliminar_duplicados()
        elif opcion == "5":
            es_palindromo()
        elif opcion == "6":
            contar_palabras()
        elif opcion == "7":
            encontrar_mayor()
        elif opcion == "8":
            invertir_lista()
        elif opcion == "9":
            filtrar_pares()
        elif opcion == "10":
            encontrar_segundo_mayor()
        elif opcion == "11":
            contar_vocales()
        elif opcion == "12":
            ordenar_tuplas()
        elif opcion == "13":
            contar_unicos()
        elif opcion == "14":
            palabras_mas_largas()
        elif opcion == "15":
            es_primo()
        elif opcion == "S":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, Intente de nuevo.")
menu()




