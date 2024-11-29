import tkinter as tk 
root = tk. Tk()
label = tk.label(root, text="Texto personalizado", font=("Helvetica", 16), fg= "pink" )
label.pack()

button = tk.Button(root, text="boton estilizado", bg="gray" )
button.pack()

root.mainloop()