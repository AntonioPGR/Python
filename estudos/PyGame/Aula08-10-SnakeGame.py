import pygame
from pygame.locals import *
from random import randint
from sys import exit
from time import sleep


def desenha_cobra(posicoes):
    for posicao in posicoes:
        pygame.draw.rect(tela, (5, 255, 0), (posicao[0], posicao[1], 20, 20))


def game_over():
    global morreu
    morreu = True
    pygame.mixer.Sound('musicas/mixkit-retro-arcade-game-over-470.wav').play()

    while morreu:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                exit()
            if ev.type == KEYDOWN:
                if ev.key == K_r:
                    reiniciar_jogo()

        tela.fill((255, 255, 255))
        fonte_go = pygame.font.SysFont('Arial', 100, True, False)
        fonte_pnts_go = pygame.font.SysFont('Arial', 30, True, False)

        go_msg = fonte_go.render('Game Over', True, (255, 0, 0))
        pnts_msg = fonte_pnts_go.render(f'pontuação: {pontos}', True, (255, 0, 0))
        restart_msg = fonte_pnts_go.render('Aperte R para reiniciar', True, (255, 0, 0))

        rect_go = go_msg.get_rect()
        rect_go.center = (400, 200)
        rect_pnts = pnts_msg.get_rect()
        rect_pnts.center = (400, 300)
        rect_restart = restart_msg.get_rect()
        rect_restart.center = (400, 350)

        tela.blit(go_msg, rect_go)
        tela.blit(pnts_msg, rect_pnts)
        tela.blit(restart_msg, rect_restart)
        pygame.display.update()


def reiniciar_jogo():
    global pontos, cobra_p, lista_cobra, comprimento_max, last_key, morreu, racao_p
    pontos = 0
    cobra_p['x'] = 350
    cobra_p['y'] = 290
    racao_p['x'] = randint(30, 750)
    racao_p['y'] = randint(30, 550)
    lista_cobra = []
    comprimento_max = 5
    last_key = ''
    morreu = False


# Configurações da tela
pygame.init()
dimensoes = (800, 600)
tela = pygame.display.set_mode(dimensoes)
fps = pygame.time.Clock()

# posições
racao_p = {'x': randint(30, 750), 'y': randint(30, 550)}
cobra_p = {'x': 350, 'y': 290}

# Pontuação
pontos = 0
fonte_pnts = pygame.font.SysFont('Arial', 36, True, False)

# Musicaa
# pygame.mixer.music.load('musicas/Corona-320bit.mp3')
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.1)

msc_pnt = pygame.mixer.Sound('musicas/smw_coin.wav')

# Aumentar Cobra
lista_cobra = []
comprimento_max = 5
last_key = ''
x_control = 5
y_control = 0
velocidade = 5

#  GameOver
morreu = False

while True:
    velocidade = 5 + pontos / 20
    fps.tick(60)
    tela.fill((255, 255, 255))

    # Exibir pontuação
    msg = f'Pontos: {pontos}'
    text = fonte_pnts.render(msg, False, (0, 0, 0))
    tela.blit(text, (5, 5))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                if last_key != 'down':
                    last_key = 'up'
                    y_control = -velocidade
                    x_control = 0

            if event.key == K_DOWN:
                if last_key != 'up':
                    last_key = 'down'
                    y_control = velocidade
                    x_control = 0

            if event.key == K_LEFT:
                if last_key != 'right':
                    last_key = 'left'
                    x_control = -velocidade
                    y_control = 0

            if event.key == K_RIGHT:
                if last_key != 'left':
                    last_key = 'right'
                    x_control = velocidade
                    y_control = 0

    cobra_p['x'] += x_control
    cobra_p['y'] += y_control
    cobra = pygame.draw.rect(tela, (0, 255, 0), (cobra_p['x'], cobra_p['y'], 20, 20))
    racao = pygame.draw.rect(tela, (255, 5, 0), (racao_p['x'], racao_p['y'], 20, 20))

    lista_cobra.append((cobra_p['x'], cobra_p['y']))

    if len(lista_cobra) > comprimento_max:
        del lista_cobra[0]

    if cobra.colliderect(racao):
        pontos += 1
        msc_pnt.play()
        comprimento_max += 2
        racao_p['x'] = randint(30, 750)
        racao_p['y'] = randint(30, 550)

    if cobra_p['x'] <= 0 or cobra_p['x'] >= 800 or cobra_p['y'] <= 0 or cobra_p['y'] >= 600:
        game_over()

    if lista_cobra.count((cobra_p['x'], cobra_p['y'])) > 1:
        game_over()

    desenha_cobra(lista_cobra)
    pygame.display.update()
