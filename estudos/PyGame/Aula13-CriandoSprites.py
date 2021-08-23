import pygame as pg
import pygame.image
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from sys import exit


class AnimarSprites(pg.sprite.Sprite):
    def __init__(self, nsprites=0, caminho=''):
        pg.sprite.Sprite.__init__(self)
        self.sprites = []
        self.preencher_sprites(nsprites, caminho)
        self.sprite_atual = 0
        self.image = self.sprites[self.sprite_atual]
        # nescecita de ser self.image pq é um atributo da clase pai que ira printar essa imagem na tela
        self.image = pg.transform.scale(self.image, (20 * 5, 30 * 5))

        self.rect = self.image.get_rect()
        self.rect.center = dimensoes[0]/2, dimensoes[1]/2

        self.animado = False

    def preencher_sprites(self, ns, caminho):
        for sprite in range(0, ns+1):
            self.sprites.append(pg.image.load(caminho.replace('XX', f'{sprite}')))

    def animar(self):
        self.animado = True

    def update(self):
        if self.animado:
            if self.sprite_atual >= len(self.sprites):
                self.sprite_atual = 0
                self.animado = False
            self.image = self.sprites[int(self.sprite_atual)]
            self.sprite_atual += 0.1
            self.image = pg.transform.scale(self.image, (20 * 5, 30 * 5))


# tela
pg.init()
dimensoes = (600, 300)
tela = pg.display.set_mode(dimensoes)
fps = pg.time.Clock()
backgroung = pygame.image.load('Sprites/demonio/background.jpg')
backgroung = pygame.transform.scale(backgroung, (600, 300))

# sprites
group = pg.sprite.Group()
demonio = AnimarSprites(6, 'Sprites/demonio/sprite_XX.png')
group.add(demonio)

while True:
    tela.fill((255, 255, 255))
    tela.blit(backgroung, (0, 0))
    fps.tick(80)
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            demonio.animar()

    group.draw(tela)
    group.update()
    pg.display.flip()

