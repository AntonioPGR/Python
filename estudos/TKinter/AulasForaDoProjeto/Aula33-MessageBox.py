from tkinter import *
from tkinter import messagebox

root = Tk()


def display():
    messagebox.showinfo('info', 'só para você saber')
    messagebox.showwarning('Perigo', 'Melhor ter cuidado')
    messagebox.showerror('Erro', 'Algo deu errado')

    okcancel = messagebox.askokcancel('O que você acha?', 'devemos ir em frente?')
    print(okcancel)

    yesno = messagebox.askyesno('Sim ou não', 'por favor decida')
    print(yesno)

    retrycancel = messagebox.askretrycancel('Sim ou não', 'qual sua resposta?')
    print(retrycancel)

    answer = messagebox.askquestion('Eai, tudo bom?', 'fala ai')
    print(answer)


b1 = Button(root, text='Exibir dialogos', command=display)
b1.pack()

root.mainloop()
