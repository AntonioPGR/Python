import pygame as pg
from random import randrange
from os.path import join

pg.mixer.init()


class Dino(pg.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pg.sprite.Sprite.__init__(self)

        # som
        self.sound_jump = pg.mixer.Sound(join('audio/sons_jump_sound.wav'))
        self.sound_death = pg.mixer.Sound(join('audio/sons_death_sound.wav'))

        # Adicionar Sprites a lista
        self.sprites_dino_andando = []
        self.sprites_dino_piscando = []
        self.sprite_dino_gameover = sprite_sheet.subsurface((32*4, 32*0), (32, 32))
        self.__add_sprites(sprite_sheet)

        # Configuração de imagem
        self.posicao_atual = 0
        self.image = self.sprites_dino_piscando[self.posicao_atual]
        self.image = pg.transform.scale(self.image, (32 * 3, 32 * 3))
        self.rect = self.image.get_rect()
        self.posicao_inicial = (100, 470)
        self.rect.bottomleft = 100, 470
        self.mask = pg.mask.from_surface(self.image)

        # Variaveis de controle
        self.run = True
        self.jump = False
        self.subindo = False
        self.gameover = False
        self.flutuar = 0
        self.velocidade = 0

    def __add_sprites(self, spr_sheet):
        for i in range(2):
            img = spr_sheet.subsurface(((32 * i), 0), (32, 32))
            self.sprites_dino_piscando.append(img)

        for i in range(2, 4):
            img = spr_sheet.subsurface(((32 * i), 0), (32, 32))
            self.sprites_dino_andando.append(img)

    def update(self):
        if not self.gameover:
            if self.run and not self.jump:
                self.__andar()
            elif not self.run and not self.jump:
                self.__piscar()

            if self.jump:
                self.__pular()

    def __piscar(self):
        if self.posicao_atual >= len(self.sprites_dino_piscando):
            self.posicao_atual = 0

        self.image = self.sprites_dino_piscando[int(self.posicao_atual)]
        self.image = pg.transform.scale(self.image, (32 * 3, 32 * 3))

        if int(self.posicao_atual) == 0:
            self.posicao_atual += 0.01
        elif int(self.posicao_atual) == 1:
            self.posicao_atual += 0.05

    def comecar_andar(self):
        self.run = True

    def __andar(self):
        if self.posicao_atual >= len(self.sprites_dino_andando):
            self.posicao_atual = 0

        self.image = self.sprites_dino_andando[int(self.posicao_atual)]
        self.image = pg.transform.scale(self.image, (32 * 3, 32 * 3))

        self.posicao_atual += 0.2

    def comecar_pular(self):
        self.jump = True
        self.subindo = True

    def __pular(self):
        if self.rect.bottomleft[1] <= 250:
            if self.subindo:
                self.sound_jump.play()
            self.subindo = False
            self.flutuar += 1

        if self.subindo:
            self.rect.y -= 17
        else:
            if not self.subindo and self.flutuar >= 10:
                self.rect.y += 17

        if self.rect.bottomleft[1] >= self.posicao_inicial[1]:
            self.rect.bottomleft = self.posicao_inicial
            self.jump = False
            self.flutuar = 0

    def setgameover(self):
        if not self.gameover:
            self.sound_death.play()
            self.image = self.sprite_dino_gameover
            self.image = pg.transform.scale(self.image, (32 * 3, 32 * 3))
        self.gameover = True

    def setVelocidade(self, vel):
        self.velocidade = vel


class Nuvens(pg.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pg.sprite.Sprite.__init__(self)

        self.sprite_nuvem = sprite_sheet.subsurface((32 * 3, 32), (32, 32))
        self.image = pg.transform.scale(self.sprite_nuvem, (32 * 3, 32 * 3))

        self.x = randrange(100, 900, 100)
        self.y = randrange(0, 120, 30)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        self.gameover = False
        self.velocidade = 0

    def update(self):
        if not self.gameover:
            if self.rect.topright[0] < 0:
                self.x = randrange(1000, 1200, 50)
                self.y = randrange(0, 150, 30)
            self.x -= self.velocidade
            self.rect.topleft = self.x, self.y

    def setVelocidade(self, vel):
        self.velocidade = vel

    def setgameover(self):
        self.gameover = True


class Chao(pg.sprite.Sprite):
    def __init__(self, sprite_sheet, num):
        pg.sprite.Sprite.__init__(self)

        self.sprite_chao = sprite_sheet.subsurface((32 * 4, 32), (32, 32))
        self.image = pg.transform.scale(self.sprite_chao, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.topleft = num * 64, 436

        self.gameover = False
        self.velocidade = 0

    def update(self):
        if not self.gameover:
            if self.rect.topright[0] < 0:
                self.rect.x = 1000 - self.velocidade
            self.rect.x -= self.velocidade

    def setVelocidade(self, vel):
        self.velocidade = vel

    def setgameover(self):
        self.gameover = True


class Cactos(pg.sprite.Sprite):
    def __init__(self, spritesheet):
        pg.sprite.Sprite.__init__(self)

        self.cacto_sprite = spritesheet.subsurface((32 * 2, 32), (32, 32))
        self.tamanho_atual = 3
        self.image = pg.transform.scale(self.cacto_sprite, (32 * self.tamanho_atual, 32 * self.tamanho_atual))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = 1000, 470
        self.last_pos = 1000
        self.mask = pg.mask.from_surface(self.image)

        self.gameover = False
        self.escolha = -1
        self.velocidade = 0

    def update(self):
        if not self.gameover and self.escolha == 0:
            if self.rect.x <= 0 - (self.tamanho_atual * 32):
                self.rect.x = 1000 + self.velocidade
                self.escolha = -1
            self.rect.x -= self.velocidade

    def setVelocidade(self, vel):
        self.velocidade = vel

    def setescolha(self, escolha):
        if escolha == 0:
            self.escolha = escolha

    def setgameover(self):
        self.gameover = True


class Pterodactil(pg.sprite.Sprite):
    def __init__(self, spritesheet):
        pg.sprite.Sprite.__init__(self)
        self.sprites_pter = []
        self.add_sprites(spritesheet)
        self.pos_atual = 0
        self.image = self.sprites_pter[self.pos_atual]
        self.image = pg.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = 1000, 300

        self.gameover = False
        self.escolha = -1
        self.velocidade = 0

    def update(self):
        if not self.gameover and self.escolha == 1:
            if self.rect.bottomright[0] < 0:
                self.rect.bottomleft = 1000 + self.velocidade, randrange(300, 451, 150)
                self.escolha = -1
            self.rect.x -= self.velocidade
            self.animar()

    def setVelocidade(self, vel):
        self.velocidade = vel

    def setescolha(self, escolha):
        if escolha == 1:
            self.escolha = escolha

    def animar(self):
        self.pos_atual += 0.1
        if self.pos_atual >= 2:
            self.pos_atual = 0
        self.image = self.sprites_pter[int(self.pos_atual)]
        self.image = pg.transform.scale(self.image, (32*3, 32*3))

    def add_sprites(self, spritesheet):
        for i in range(0, 2):
            print(i)
            self.sprites_pter.append(spritesheet.subsurface((32*i, 32), (32, 32)))

    def setgameover(self):
        self.gameover = True