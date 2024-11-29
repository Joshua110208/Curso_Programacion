# Descripción del Código

El programa pide al usuario que ingrese tres números, luego calcula el promedio de estos números y compara cada uno de ellos con el promedio, indicando si es mayor, menor o igual.

## Errores Encontrados y Soluciones

1. **Conversión de los elementos de `numeros` a `float`**:
   - **Error**: En `calcular_promedio`, la lista `numeros` no se convertía a `float` antes de la operación matemática. `input()` devuelve valores de tipo `str`, lo que provoca un error al intentar sumar directamente cadenas.
   - **Corrección**: Convertimos cada elemento de `numeros` a `float` al inicio de `calcular_promedio`.

2. **Sintaxis de condicionales `if`, `elif`, y `else` en `comparar_con_promedio`**:
   - **Error**: Los condicionales `if`, `elif`, y `else` carecían de dos puntos (`:`) al final, lo cual es obligatorio en Python para delimitar el bloque de código.
   - **Corrección**: Agregamos los dos puntos al final de cada línea de condición.

3. **Conversión de entrada del usuario a `float` en el bucle de `input()`**:
   - **Error**: Al almacenar cada número en `numeros`, los valores ingresados no se convertían a tipo `float`, lo cual causaba problemas al tratar de realizar cálculos numéricos.
   - **Corrección**: Convertimos `num` a `float` justo después de obtener el valor con `input()` y antes de agregarlo a la lista `numeros`. Esto asegura que `numeros` contenga valores numéricos válidos para las operaciones posteriores.

Este `README` explica cada error identificado, la corrección aplicada y su justificación.