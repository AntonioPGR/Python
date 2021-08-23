import pygame
from pygame.locals import *
from sys import exit

pygame.init()

dimensoes = (500, 300)
tela = pygame.display.set_mode(dimensoes)
pygame.display.set_caption('Its me, Mario!')


class AnimarSprites(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.preencher_sprites()
        self.sprite_atual = 0
        self.image = self.sprites[self.sprite_atual]  # nescecita de ser self.image pq é um atributo da clase pai que ira printar essa imagem na tela
        self.image = pygame.transform.scale(self.image, (20 * 3, 30 * 3))

        self.rect = self.image.get_rect()
        self.rect.center = 250, 150

        self.animar = False

    def preencher_sprites(self):
        self.sprites.append(pygame.image.load('Sprites/mario/mario_andando01.png'))
        self.sprites.append(pygame.image.load('Sprites/mario/mario_andando02.png'))
        self.sprites.append(pygame.image.load('Sprites/mario/mario_andando03.png'))

    def andar(self):
        self.animar = True

    def update(self):
        if self.animar:
            if self.sprite_atual >= len(self.sprites):
                self.sprite_atual = 0
                self.animar = False
            self.image = self.sprites[int(self.sprite_atual)]
            self.sprite_atual += 0.09
            self.image = pygame.transform.scale(self.image, (20 * 3, 30 * 3))


sprites = pygame.sprite.Group()
mario = AnimarSprites()
sprites.add(mario)

fps = pygame.time.Clock()

while True:
    fps.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            mario.andar()

    sprites.draw(tela)
    sprites.update()

    pygame.display.flip()
