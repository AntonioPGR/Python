from Modulos import *

class Relatorios:
    @staticmethod
    def printCliente():
        webbrowser.open("cliente.pdf")

    def GeraRelatorio(self):
        c = canvas.Canvas("cliente.pdf")
        cod = self.et_code.get()
        nome = self.et_nome.get()
        tel = self.et_telefone.get()
        cid = self.et_cidade.get()

        c.setFont('Helvetica-Bold', 24)
        c.drawString(200, 790, 'Ficha do Cliente')

        c.setFont('Helvetica-Bold', 14)
        c.drawString(50, 740, 'Codigo:')
        c.drawString(50, 710, 'Nome:')
        c.drawString(50, 680, 'Telefone:')
        c.drawString(50, 650, 'Cidade:')

        c.setFont('Helvetica', 14)
        c.drawString(105, 740, f'{cod}')
        c.drawString(95, 710, f'{nome}')
        c.drawString(115, 680, f'{tel}')
        c.drawString(105, 650, f'{cid}')

        c.rect(20, 625, 550, 150, fill=False, stroke=True)

        c.showPage()
        c.save()
        self.printCliente()