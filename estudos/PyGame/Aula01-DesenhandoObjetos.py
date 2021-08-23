import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = (800, 500)
tela = pygame.display.set_mode(largura)
pygame.display.set_caption('Super jogo bros')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (0, 255, 0), (300, 200, 100, 200))  # tela, cor, (posiçãoX (horizontal), posiçãoY (vertical) do px sup esq, largura, altura)
    pygame.draw.circle(tela, (120, 0, 120), (200, 250), 50)  # (pX, pY do Meio do circulo), raio
    pygame.draw.line(tela, (150, 150, 20), (450, 50), (450, 400), 5)  # (pX,pY de inicio), (pX, pY de fim), espessura )

    pygame.display.update()
