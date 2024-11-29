import tkinter as tk 
root = tk. Tk()
label = tk.label(root, text="Bienvenido a Tkinder :3")
label.pack()

entry = tk.Entry(root)
entry.pack()


button = tk.Button(root, text="presionar")
button.pack()

root.mainloop()
