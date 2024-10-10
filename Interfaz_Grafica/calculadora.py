import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta cuando un botón es presionado
def on_click(symbol):
    current = entry.get()  # Obtiene el contenido actual del cuadro de entrada

    if symbol == 'C':  # Si el símbolo presionado es 'C' (limpiar)
        entry.delete(0, tk.END)  # Borra todo el contenido del cuadro de entrada

    elif symbol == '=':  # Si el símbolo presionado es '=' (calcular resultado)
        try:
            result = eval(current)  # Evalúa la expresión matemática
            entry.delete(0, tk.END)  # Limpia el cuadro de entrada
            entry.insert(tk.END, str(result))  # Inserta el resultado
        except Exception as e:
            # Si hay un error (ej. operación inválida), muestra un mensaje de error
            messagebox.showerror('Error', 'Operación inválida')
    else:
        entry.insert(tk.END, symbol)  # Inserta el símbolo presionado en la pantalla

# Configuración de la ventana principal (calculadora)
root = tk.Tk()  # Inicializa la ventana principal de Tkinter
root.title("Calculadora")
root.configure(bg='#b3b3b3')  # Fondo gris claro para la calculadora

# Configuración del cuadro de entrada (fuente cursiva y margen oscuro)
entry = tk.Entry(root, width=35, borderwidth=5, font=('Georgia', 18, 'italic'), justify='right')
# El cuadro de entrada usa la fuente 'Georgia' en cursiva, con un tamaño de 18.
# justify='right' alinea el texto a la derecha, como en una calculadora estándar
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  
# Coloca el cuadro de entrada en la primera fila (row=0) y abarca 4 columnas (columnspan=4)

# Lista de botones de la calculadora
buttons = [
    '7', '8', '9', '/',  # Fila 1: Números 7, 8, 9 y el operador de división
    '4', '5', '6', '*',  # Fila 2: Números 4, 5, 6 y el operador de multiplicación
    '1', '2', '3', '-',  # Fila 3: Números 1, 2, 3 y el operador de resta
    'C', '0', '=', '+'   # Fila 4: Botón 'C' (limpiar), número 0, igual '=' y operador de suma
]

# Variables que controlan la ubicación de los botones en la cuadrícula
row_val = 1  # La primera fila de botones comienza en la fila 1
col_val = 0  # La primera columna de botones comienza en la columna 0

# Ciclo que crea y configura cada botón
for button in buttons:
    action = (lambda x=button: on_click(x))  # Define la acción de cada botón usando la función on_click
    
    # Configuración de cada botón con propiedades estilísticas
    b = tk.Button(root, text=button, padx=20, pady=20, font=('Verdana', 18, 'italic'), command=action,
                  bg='#ff66b2',  # Color de fondo rosa
                  fg='#000000',  # Texto negro
                  activebackground='#ff99cc',  # Fondo rosa claro cuando el botón es presionado
                  bd=5,  # Borde con grosor de 5 píxeles
                  relief='solid',  # Relieve sólido para los bordes de los botones
                  highlightbackground='#404040',  # Borde gris oscuro alrededor de los botones
                  highlightthickness=2)  # Grosor del borde gris oscuro
    
    b.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)  
    # Coloca el botón en la cuadrícula, con un pequeño margen (5px) alrededor
    
    col_val += 1  # Mueve el siguiente botón a la siguiente columna
    if col_val > 3:  # Si llega a la cuarta columna, resetea a la columna 0 y mueve a la siguiente fila
        col_val = 0
        row_val += 1

# Configuración de la cuadrícula para distribuir los botones uniformemente
for i in range(4):
    root.grid_columnconfigure(i, weight=1)  # Asegura que todas las columnas se expandan uniformemente

for i in range(5):
    root.grid_rowconfigure(i, weight=1)  # Asegura que todas las filas se expandan uniformemente

# Mantiene la ventana abierta y lista para interactuar
root.mainloop()  

