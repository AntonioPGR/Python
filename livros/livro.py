from selenium import webdriver
"""Programa que vai utilizar Web Scrapping para auxiliar na busca
de livros e de resumos.
"""

class Livro:
    def __init__(self, nome, autor=""):
        # configurações de navegador:
        PATH = 'webdriver\chromedriver.exe'
        self.driver = webdriver.Chrome(PATH)

        self.nome = nome.title()
        self.autor = autor.title()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.nome!r}, {self.autor!r})"

    def __str__(self) -> str:
        return f"O livro escolhido é o: {self.nome}, escrito por {self.autor}"

    def procurar_livro(self):
        self.driver.get('https://www.youtube.com')
        self.driver.get('https://www.google.com')
        self.driver.quit()

    def resumo_livro(self):
        """Procura por um resumo do livro escolhido no site
        'https://educacao.uol.com.br/resumos-de-livros/'.
        Caso haja um resumo, retorna um link para acessá-lo."""
        pass


l1 = Livro('um dia em marte')
l1.procurar_livro()