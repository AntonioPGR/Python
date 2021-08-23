import pygame
from pygame.locals import *
from random import randint
from sys import exit
from time import sleep

pygame.init()

dimensoes = (800, 500)
br = False

ret_verde_x = int(dimensoes[0] / 2 - 25)
ret_verde_y = int(dimensoes[1] / 2 - 20)
ret_verm_x = randint(10, 750)
ret_verm_y = randint(10, 440)

pygame.mixer.music.set_volume(0.1)  # alterar volume da musica de background
pygame.mixer.music.load('musicas/BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)  # passando -1, a musica ficara em looping

musica_colisao = pygame.mixer.Sound('musicas/smw_coin.wav')

pontos = 0
fonte1 = pygame.font.SysFont('Times', 36, True, False)  # fonte, tamanho, negrito, itálico
fonte2 = pygame.font.SysFont('Arial', 80, True, False)

tela = pygame.display.set_mode(dimensoes)
pygame.display.set_caption('Super jogo bros')
fps = pygame.time.Clock()

while True:
    if br:
        sleep(5)
        break

    fps.tick(50)
    tela.fill((0, 0, 0))
    msg = f'Pontos = {pontos}'
    pnts = fonte1.render(msg, True, (255, 255, 255))  # msg, pixelado? True == não, cor

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
        musica_colisao.play()
    if pontos >= 10:
        msg = f'Você Venceu!'
        vit = fonte2.render(msg, True, (150, 150, 0))
        tela.blit(vit, (150, 150))
        br = True

    tela.blit(pnts, (5, 5))
    pygame.display.update()
