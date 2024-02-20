from django.shortcuts import render
from django.http import HttpResponse

# Ejercicio 1. Desarrolla un código que calcule el área de un triángulo.
def areatriangulo(request):
    base = int (request.GET.get('base', 1))
    altura = int (request.GET.get('altura', 1))
    calculo = base * altura / 2
    vista = (f"El area del triangulo es {calculo}")
    return HttpResponse(vista)

# Ejercicio 2. Crea un código que calcule el área de un rectángulo.
def arearectangulo(request):
    lado1 = int (request.GET.get('lado1', 1))
    lado2 = int (request.GET.get('lado2', 1))
    calculo = lado1 * lado2
    vista = (f"El area del rectangulo es {calculo}")
    return HttpResponse(vista)

# Ejercicio 3. Desarrolla un algoritmo que calcule el área de un círculo.
def areacirculo(request):
    radio = float (request.GET.get('radio', 1))
    calculo = radio * radio * 3.1415
    vista = (f"El area del circulo es {calculo}")
    return HttpResponse(vista)

# Ejercicio 4. Desarrolla un código que calcule la longitud de un triángulo sabiendo sus lados.
def longitudtriangulo(request):
    lado1 = int (request.GET.get('lado1', 1))
    lado2 = int (request.GET.get('lado2', 1))
    lado3 = int (request.GET.get('lado3', 1))
    calculo = lado1 + lado2 + lado3
    vista = (f"El perimetro del triangulo es {calculo}")
    return HttpResponse(vista)

# Ejercicio 5. Crea un código que calcule la longitud de un rectángulo sabiendo sus lados.
def longitudrectangulo(request):
    lado1 = int (request.GET.get('lado1', 1))
    lado2 = int (request.GET.get('lado2', 1))
    calculo = lado1 + lado1 + lado2 + lado2
    vista = (f"El perimetro del rectangulo es {calculo}")
    return HttpResponse(vista)

# Ejercicio 6. Crea un código que calcule la longitud de un cuadrado sabiendo sólo un lado.
def longitudcuadrado(request):
    lado1 = int (request.GET.get('lado1', 1))
    calculo = lado1 * 4
    vista = (f"El perimetro del cuadrado es {calculo}")
    return HttpResponse(vista)

# Ejercicio 7. Desarrolla un algoritmo que calcule la longitud de un círculo sabiendo su radio.
def longitudcirculo(request):
    radio = float (request.GET.get('radio', 1))
    calculo = 2 * radio * 3.1415
    vista = (f"El perimetro del circulo es {calculo}")
    return HttpResponse(vista)

# Ejercicio 8. Escribe un script que cuente la cantidad de vocales en una palabra.
def cantidadvocales(request):
    palabra = request.GET.get('palabra', '')
    # Convertimos la palabra a minúsculas para hacer la comparación de manera uniforme
    palabra = palabra.lower()
    
    # Contador para almacenar el número de vocales
    nvocales = 0
    
    # Lista de vocales
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    # Iteramos sobre cada caracter en la palabra y contamos las vocales
    for letra in palabra:
        if letra in vocales:
            nvocales += 1
    
    # Creamos la cadena de respuesta con el número de vocales encontradas
    vista = f"Número de vocales de la palabra '{palabra}' = {nvocales}"
    
    return HttpResponse(vista)

# Ejercicio 9. Diseña un algoritmo para encontrar el mínimo de un conjunto de números.
def minimo(request):
    # Obtenemos la cadena de números separados por comas de la consulta GET
    numeros_str = request.GET.get('numeros', '')
    
    # Verificamos si la cadena está vacía
    if not numeros_str:
        return HttpResponse("No se proporcionaron números.")
    
    # Convertimos la cadena en una lista de números enteros
    numeros = [int(num) for num in numeros_str.split(',')]
    
    # Comprobamos si no se proporcionaron números
    if not numeros:
        return HttpResponse("No se proporcionaron números válidos.")
    
    # Inicializamos el mínimo como el primer número
    minimo_valor = numeros[0]
    
    # Iteramos sobre los números restantes
    for num in numeros[1:]:
        # Si encontramos un número menor, actualizamos el mínimo
        if num < minimo_valor:
            minimo_valor = num
    
    return HttpResponse(f"El mínimo de los números proporcionados es: {minimo_valor}")

# Ejercicio 10. Implementa un programa que determine si un número es positivo, negativo o cero.
def posnegcero(request):
    # Obtenemos el número de la consulta GET
    numero_str = request.GET.get('numero', '')
    
    # Verificamos si no se proporcionó un número
    if not numero_str:
        return HttpResponse("No se proporcionó un número.")
    
    # Convertimos el número a un valor entero
    try:
        numero = int(numero_str)
    except ValueError:
        return HttpResponse("El valor proporcionado no es un número válido.")
    
    # Determinamos el signo del número
    if numero > 0:
        signo = "positivo"
    elif numero < 0:
        signo = "negativo"
    else:
        signo = "cero"
    
    return HttpResponse(f"El número proporcionado es {signo}.")
