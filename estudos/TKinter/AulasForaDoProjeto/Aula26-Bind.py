from tkinter import *
from tkinter import ttk

root = Tk()

l = ttk.Label(root, text='Começando...')
l.grid()

l.bind("<Enter>", lambda e: l.configure(text='Mouse entrou'))
l.bind("<Leave>", lambda e: l.configure(text='Mouse saiu'))
l.bind("<1>", lambda e: l.configure(text='Clicou com botão\nesquerdo do mouse'))
l.bind("<Double-1>", lambda e: l.configure(text='Duplo clique com o mouse'))
l.bind("<B3-Motion>", lambda e: l.configure(text='Arraste o botão \n direito para %d,%d' % (e.x, e.y)))

root.mainloop()
