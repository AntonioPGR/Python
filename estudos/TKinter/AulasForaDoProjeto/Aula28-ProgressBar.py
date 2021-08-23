from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title('progress bar')
root.geometry('500x400')


def step():
    #  progress1['value'] += 10
    #  progress1.start(30)
    for x in range(20):
        progress1['value'] += 10
        root.update_idletasks()
        time.sleep(0.5)


def stop():
    progress1.stop()


progress1 = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
progress1.pack(pady=20)

botao = Button(root, text='progresso', command=step)
botao.pack(pady=20)

botao2 = Button(root, text='parar', command=stop)
botao2.pack(pady=20)

root.mainloop()
