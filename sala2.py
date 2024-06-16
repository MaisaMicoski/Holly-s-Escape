import pygame

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.gameobject import *
from PPlay.mouse import *
import random
from jogador import *
class Sala2:

    def __init__(self):
        self.sala2 = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('sala1')
        self.saiu = False
        self.fundo = pygame.Color('black')
        self.mesa1 = pygame.image.load('mesa.png')
        self.mesa2 = pygame.image.load('mesa.png')
        self.mesa3 = pygame.image.load('mesa.png')
        self.mesa4 = pygame.image.load('mesa.png')

        self.mesa1 = pygame.transform.scale(self.mesa1, (int(self.mesa1.get_width() * 1.8), int(self.mesa1.get_height() * 1.8)))
        self.mesa1_rect = self.mesa1.get_rect()

        self.mesa1_rect.topleft = (290,220)

        self.mesa2 = pygame.transform.scale(self.mesa2,
                                            (int(self.mesa2.get_width() * 1.8), int(self.mesa2.get_height() * 1.8)))
        self.mesa2_rect = self.mesa2.get_rect()

        self.mesa2_rect.topleft = (680, 220)

        self.mesa3 = pygame.transform.scale(self.mesa3,
                                            (int(self.mesa3.get_width() * 1.8), int(self.mesa3.get_height() * 1.8)))
        self.mesa3_rect = self.mesa3.get_rect()

        self.mesa3_rect.topleft = (290, 470)

        self.mesa4 = pygame.transform.scale(self.mesa4,
                                            (int(self.mesa4.get_width() * 1.8), int(self.mesa4.get_height() * 1.8)))
        self.mesa4_rect = self.mesa4.get_rect()

        self.mesa4_rect.topleft = (680, 470)
        clock = pygame.time.Clock()
        FPS = 60

        self.chao = pygame.image.load('sala1.png')
        self.chao = pygame.transform.scale(self.chao, (int(self.chao.get_width() * 2), int(self.chao.get_height() * 2)))
        self.chao_rect = self.chao.get_rect()

        self.chao_rect.topleft = (210, 0)


        self.holly = Holly(950, self.sala2.get_height()-80,1, 4, 4)


        self.movimento_esquerda = False
        self.movimento_direita = False
        self.movimento_up = False
        self.movimento_down = False
    def loop_principal(self):
        run = True

        while run:

            self.sala2.fill(self.fundo)

            self.sala2.blit(self.chao, self.chao_rect.topleft)

            self.sala2.blit(self.mesa1, self.mesa1_rect.topleft)
            self.sala2.blit(self.mesa2, self.mesa2_rect.topleft)
            self.sala2.blit(self.mesa3, self.mesa3_rect.topleft)
            self.sala2.blit(self.mesa4, self.mesa4_rect.topleft)

            self.holly.desenha(self.sala2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False  # saida
                    if event.key == pygame.K_a:
                        self.movimento_esquerda = True
                    if event.key == pygame.K_e:
                        if self.holly.rect.bottom  >= 680 and self.holly.rect.left > 900 and self.holly.rect.left < 930:
                            run = False
                    if event.key == pygame.K_d:
                        self.movimento_direita = True

                    if event.key == pygame.K_w:
                        self.movimento_up = True
                    if event.key == pygame.K_s:
                        self.movimento_down = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movimento_esquerda = False
                    if event.key == pygame.K_d:
                        self. movimento_direita = False
                    if event.key == pygame.K_w:
                        self.movimento_up = False
                    if event.key == pygame.K_s:
                        self.movimento_down = False

            if self.holly.rect.right+20 >= self.chao_rect.right:
                self.movimento_direita = False
            if self.holly.rect.left-20 <= self.chao_rect.left:
                self.movimento_esquerda = False
            if self.holly.rect.bottom+20 >= self.chao_rect.bottom:
                self.movimento_down = False
            if self.holly.rect.bottom <= 200:
                self.movimento_up = False

            if (self.holly.colisaoB(self.mesa1_rect) or self.holly.colisaoB(self.mesa2_rect) or
                    self.holly.colisaoB(self.mesa3_rect) or self.holly.colisaoB(self.mesa4_rect)):
                self.movimento_up = False

            if (self.holly.colisaoC(self.mesa1_rect) or self.holly.colisaoC(self.mesa2_rect) or
                    self.holly.colisaoC(self.mesa3_rect) or self.holly.colisaoC(self.mesa4_rect)):
                self.movimento_down = False

            if (self.holly.colisaoE(self.mesa1_rect) or self.holly.colisaoE(self.mesa2_rect) or
                    self.holly.colisaoE(self.mesa3_rect) or self.holly.colisaoE(self.mesa4_rect)):
                self.movimento_esquerda = False

            if ((self.holly.colisaoD(self.mesa1_rect)) or self.holly.colisaoD(self.mesa2_rect) or
                self.holly.colisaoD(self.mesa3_rect) or self.holly.colisaoD(self.mesa4_rect)):
                self.movimento_direita = False

            self.holly.movimento(self.movimento_esquerda, self.movimento_direita, self.movimento_up,self. movimento_down)

            pygame.display.update()
if __name__ == "__main__":
    sala = Sala2()
    sala.loop_principal()