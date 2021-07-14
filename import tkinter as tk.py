import tkinter as tk
from tkinter import ttk
janela = tk.Tk()
janela.title("Aplicação")
ttk.Label(janela, text="Apresentação").grid(column=0, row=0)
janela.mainloop()