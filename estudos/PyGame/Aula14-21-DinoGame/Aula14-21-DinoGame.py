import pygame as pg
from pygame.locals import QUIT, KEYDOWN, K_SPACE
from sys import exit
from dino import Dino, Nuvens, Chao, Cactos, Pterodactil
from random import randint, choice
from os.path import join, dirname

# pygame
pg.init()
pg.mixer.init()

# diretorios
diretorio_principal = dirname(__file__)
diretorio_imgs = join(diretorio_principal, 'imgs')

# sons
som_pontuacao = pg.mixer.Sound(join('audio/sons_score_sound.wav'))

# tela
dimensoes = (1000, 500)
branco = (255, 255, 255)
tela = pg.display.set_mode(dimensoes)
pg.display.set_caption('Dino Game')
icon = pg.image.load(join(diretorio_imgs, 'DinoIcon.png'))
pg.display.set_icon(icon)

# tempo
fps = pg.time.Clock()

# Sprites
dino_spritesheet = pg.image.load(join(diretorio_imgs, 'Dino_SpriteSheet.png')).convert_alpha()

tds_sprites = pg.sprite.Group()
dino = Dino(dino_spritesheet)
tds_sprites.add(dino)

for i in range(randint(2, 3)):
    nuvem = Nuvens(dino_spritesheet)
    tds_sprites.add(nuvem)

for i in range(0, 20):
    chao = Chao(dino_spritesheet, i)
    tds_sprites.add(chao)

# Grupo de Colisões
grupo_colisoes = pg.sprite.Group()

for i in range(0, 3):
    Cacto = Cactos(dino_spritesheet)
    tds_sprites.add(Cacto)
    grupo_colisoes.add(Cacto)

pterodactil = Pterodactil(dino_spritesheet)
tds_sprites.add(pterodactil)
grupo_colisoes.add(pterodactil)

# pontos
pontuacao = 0
vel = 10
font = pg.font.SysFont(join('fontes/game_over.ttf'), 36, True, False)

k = 0
while True:
    fps.tick(30)
    tela.fill(branco)

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        if event.type == KEYDOWN and event.key == K_SPACE and not dino.jump:
            dino.comecar_pular()

    # colisoes
    colidiu = pg.sprite.spritecollide(dino, grupo_colisoes, False, pg.sprite.collide_mask)
    if colidiu:
        for element in tds_sprites:
            element.setgameover()
    else:
        # pontuação:
        pontuacao += 1
        if pontuacao % 100 == 0:
            som_pontuacao.play()

        # velocidade
        if vel < 30:
            vel = 10 + pontuacao * 0.01
        elif k == 0:
            k = 1
            print('vel max')
        for element in tds_sprites:
            element.setVelocidade(vel)

    text = font.render(f'{pontuacao}', True, (0, 0, 0))
    tela.blit(text, (900, 5))


    # ver qual sera o obstaculo
    c = 0
    for element in grupo_colisoes:
        if element.escolha == -1:
            c += 1
    if c == 4:
        esc = choice([0, 1])
        for element in grupo_colisoes:
            element.setescolha(esc)

    tds_sprites.draw(tela)
    tds_sprites.update()

    pg.display.flip()
