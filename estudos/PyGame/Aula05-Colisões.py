import pygame
from pygame.locals import *
from random import randint
from sys import exit

pygame.init()

dimensoes = (800, 500)
ret_verde_x = int(dimensoes[0]/2 - 25)
ret_verde_y = int(dimensoes[1]/2 - 20)
ret_verm_x = randint(10, 750)
ret_verm_y = randint(10, 440)
pontos = 0
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
        ret_verde_x -= 5
    if pygame.key.get_pressed()[K_d]:
        ret_verde_x += 5
    if pygame.key.get_pressed()[K_w]:
        ret_verde_y -= 5
    if pygame.key.get_pressed()[K_s]:
        ret_verde_y += 5

    ret_verde = pygame.draw.rect(tela, (0, 255, 0), (ret_verde_x, ret_verde_y, 40, 50))
    ret_verm = pygame.draw.rect(tela, (255, 0, 0), (ret_verm_x, ret_verm_y, 40, 50))

    if ret_verde.colliderect(ret_verm):
        ret_verm_x = randint(0, 760)
        ret_verm_y = randint(0, 450)
        pontos += 1

    pygame.display.update()