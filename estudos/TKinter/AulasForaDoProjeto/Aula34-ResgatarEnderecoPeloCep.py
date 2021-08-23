from tkinter import *
import pycep_correios


root = Tk()
root.geometry('400x300')


def cepCorreios():
    cep = cep_et.get()
    cep_et.delete(0, END)
    try:
        DadosCep = pycep_correios.get_address_from_cep(cep)
    except:
        print('dados invalidos')
    else:
        print(f"""Rua: {DadosCep['logradouro']}
Bairro: {DadosCep['bairro']}
Cidade: {DadosCep['cidade']}
Estado: {DadosCep['uf']}""")


cep_lb = Label(root, text='Cep:')
cep_lb.pack()
cep_et = Entry(root)
cep_et.pack()
cep_bt = Button(root, text='localizar cep', command=cepCorreios)
cep_bt.pack()

root.mainloop()