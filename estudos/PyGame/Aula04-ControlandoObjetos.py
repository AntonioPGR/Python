import pygame
from pygame.locals import *
from sys import exit

pygame.init()

dimensoes = (800, 500)
x = dimensoes[0]/2 - 25
y = dimensoes[1]/2 - 20
tela = pygame.display.set_mode(dimensoes)
pygame.display.set_caption('Super jogo bros')
fps = pygame.time.Clock()

while True:
    fps.tick(50)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x -= 5
    if pygame.key.get_pressed()[K_d]:
        x += 5
    if pygame.key.get_pressed()[K_w]:
        y -= 5
    if pygame.key.get_pressed()[K_s]:
        y += 5

    retangulo = pygame.draw.rect(tela, (0, 255, 0), (x, y, 40, 50))

    pygame.display.update()