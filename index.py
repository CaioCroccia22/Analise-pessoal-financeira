from tkinter import *
from tkinter import ttk

# Instancia da classe TK cria o interpretador e a janela raiz
root = Tk()


# Cria um frame widget
frm = ttk.Frame(root, padding=500)

# O metodo grid é utilizado para especificar o layout relativo
frm.grid()

# Cria o label
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

# Cria o button com metodo destroy que bota tudo na tela
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)

root.mainloop()