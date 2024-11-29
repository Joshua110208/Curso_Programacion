# Importación de bibliotecas
import random  # Biblioteca para generar números aleatorios

# Clase principal del juego
class JuegoAdivinanza:
    # Constructor de la clase: inicializa el juego
    def __init__(self):
        # Genera un número secreto aleatorio entre 1 y 100
        self.secreto_numero = random.randint(1, 100)
        # Inicializa el contador de intentos del jugador
        self.intentos_realizados = 0

    # Método para validar el número ingresado por el jugador
    def validar_numero(self, numero):
        if numero < self.secreto_numero:
            # Si el número es menor al secreto, indica que debe ser mayor
            return "Mayor", "#FFA07A"  # Mensaje y color asociado (naranja)
        elif numero > self.secreto_numero:
            # Si el número es mayor al secreto, indica que debe ser menor
            return "Menor", "#FFA07A"  # Mensaje y color asociado (naranja)
        else:
            # Si el número es igual al secreto, indica que ha acertado
            return "Acertado!", "#00FF00"  # Mensaje y color asociado (verde)

    # Método para registrar un intento y devolver el resultado
    def registrar_intento(self, numero):
        # Incrementa el contador de intentos realizados
        self.intentos_realizados += 1
        # Valida el número ingresado y obtiene el resultado
        resultado, color = self.validar_numero(numero)
        # Retorna el mensaje y el color asociado
        return resultado, color

    # Método para reiniciar el juego
    def reiniciar(self):
        # Genera un nuevo número secreto
        self.secreto_numero = random.randint(1, 100)
        # Reinicia el contador de intentos
        self.intentos_realizados = 0


# Clase que representa a un jugador
class Jugador:
    # Constructor de la clase: inicializa el jugador
    def __init__(self, nombre):
        self.nombre_del_jugador = nombre  # Nombre del jugador
        self.historial_de_partidas = []  # Historial de partidas jugadas

    # Método para dar la bienvenida al jugador
    def registrar_nombre(self):
        print(f"Bienvenido, {self.nombre_del_jugador}!")  # Mensaje de bienvenida

    # Método para registrar una partida en el historial
    def registrar_partida(self, intentos, ganado):
        self.historial_de_partidas.append({
            "intentos": intentos,  # Número de intentos en la partida
            "ganado": ganado       # Si ganó o no la partida
        })

    # Método para mostrar las estadísticas del jugador
    def mostrar_estadísticas(self):
        if not self.historial_de_partidas:
            # Si no hay partidas registradas, muestra un mensaje
            print("No hay partidas registradas aún.")
            return
        # Calcula el porcentaje de partidas ganadas
        partidas_ganadas = len([p for p in self.historial_de_partidas if p["ganado"]])
        porcentaje_ganado = (partidas_ganadas / len(self.historial_de_partidas)) * 100
        # Muestra las estadísticas al jugador
        print(f"Estadísticas de {self.nombre_del_jugador}: {porcentaje_ganado:.2f}% de aciertos")
        print(f"Número de partidas jugadas: {len(self.historial_de_partidas)}")


# Clase para manejar colores en el texto
class Decorador:
    def __init__(self, color):
        self.color = color  # Define el color que se aplicará al texto

    def aplicar(self, texto):
        # Aplica el color ANSI al texto proporcionado
        return f"\033[38;5;{self.color}m{texto}\033[0m"


# Función para crear un objeto Decorador con un color específico
def crear_decorador(color):
    return Decorador(color)


# Función para mostrar un mensaje con color
def mostrar_resultado(resultado, color):
    decorador = crear_decorador(color)  # Crea un decorador con el color especificado
    return decorador.aplicar(resultado)  # Devuelve el texto decorado


# Función para guardar las estadísticas del jugador en un archivo
def guardar_estadísticas(jugador):
    # Abre el archivo en modo escritura utilizando un contexto seguro
    with open("estadísticas.txt", "w") as archivo:
        # Escribe cada partida en una línea del archivo
        for partida in jugador.historial_de_partidas:
            archivo.write(f"Intentos: {partida['intentos']}, Ganado: {partida['ganado']}\n")


# Función para mostrar el menú principal
def mostrar_menú():
    print("1. Iniciar nueva partida")  # Opción para iniciar el juego
    print("2. Ver estadísticas")      # Opción para ver estadísticas del jugador
    print("3. Salir")                 # Opción para salir del juego


# Punto de entrada del programa
if __name__ == "__main__":
    # Crea un objeto del juego y del jugador
    juego = JuegoAdivinanza()
    jugador_del_juego = Jugador("Tu nombre")

    # Bucle principal del programa
    while True:
        mostrar_menú()  # Muestra el menú al usuario
        seleccionada = input("Elegir una opción: ")  # Solicita una opción

        if seleccionada == "1":  # Iniciar una nueva partida
            juego.reiniciar()  # Reinicia el juego
            jugador_del_juego.registrar_nombre()  # Da la bienvenida al jugador
            while True:
                try:
                    # Solicita un número al jugador
                    numero = int(input("Adivina el número secreto: "))
                    # Valida el número y obtiene el resultado
                    resultado, color = juego.registrar_intento(numero)
                    print(mostrar_resultado(resultado, color))  # Muestra el resultado
                    if resultado == "Acertado!":  # Si acierta, registra la partida
                        jugador_del_juego.registrar_partida(juego.intentos_realizados, True)
                        break
                except ValueError:
                    # Si el jugador ingresa algo no válido, muestra un error
                    print("Por favor, introduce un número válido.")
        elif seleccionada == "2":  # Ver estadísticas
            jugador_del_juego.mostrar_estadísticas()  # Muestra las estadísticas
        elif seleccionada == "3":  # Salir del juego
            print("\033[91mGame Over\033[0m")  # Mensaje de salida
            guardar_estadísticas(jugador_del_juego)  # Guarda las estadísticas
            break  # Sale del bucle principal
        else:
            # Si la opción no es válida, muestra un mensaje de error
            print("\033[91mOpción inválida\033[0m")
