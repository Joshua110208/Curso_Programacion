def calcular_promedio(numeros):
    # Conversión de los elementos a float para realizar cálculos matemáticos
    numeros = [float(num) for num in numeros]
    return sum(numeros) / len(numeros)

def comparar_con_promedio(numeros, promedio):
    for num in numeros:
        # Corrección: Agregamos dos puntos al final de la línea para completar la sintaxis
        if num > promedio:
            print(f"{num} es mayor que el promedio.")
        # Corrección: Agregamos dos puntos al final de la línea para completar la sintaxis
        elif num < promedio:
            print(f"{num} es menor que el promedio.")
        # Corrección: Agregamos dos puntos al final de la línea para completar la sintaxis
        else:
            print(f"{num} es igual al promedio.")

# Pedir al usuario tres números
numeros = []
for i in range(3):
    # Conversión del input a float para asegurar que se introducen números
    num = float(input("Introduce un número: "))
    numeros.append(num)

# Calcular el promedio
promedio = calcular_promedio(numeros)

# Comparar cada número con el promedio
comparar_con_promedio(numeros, promedio)
