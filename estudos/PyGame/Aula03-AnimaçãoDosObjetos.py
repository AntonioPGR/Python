import pygame
from pygame.locals import *
from sys import exit

pygame.init()

dimensoes = (800, 500)
x = int(dimensoes[0]/2) - 25
y = -50
tela = pygame.display.set_mode(dimensoes)
pygame.display.set_caption('Super jogo bros')
fps = pygame.time.Clock()

while True:
    # fps.tick(60) taxa de frames por segundo. serve para controlar a velocidade do jogo tbm
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    retangulo = pygame.draw.rect(tela, (0, 255, 0), (x, y, 40, 50))  # tela, cor, (posiçãoX (horizontal), posiçãoY (vertical) do px sup esq, largura, altura)
    y += 0.2
    if y >= dimensoes[1]:
        y = -50

    pygame.display.update()
