import pygame

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.gameobject import *
from PPlay.mouse import *
import random

from camera import CameraGroup
from jogador import *

class Banheiro:

    def __init__(self):

        self.banheiro = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('banheiro')
        self.saiu = False
        self.fundo = pygame.Color('black')
        self.movimento_esquerda = False
        self.movimento_direita = False
        self.movimento_up = False
        self.movimento_down = False
        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.chao = pygame.image.load('banheirobase.png')
        self.chao = pygame.transform.scale(self.chao, (int(self.chao.get_width() * 2), int(self.chao.get_height() * 2)))
        self.chao_rect = self.chao.get_rect()

        self.chao_rect.topleft = (100,100)
        self.holly = Holly(145, 505, 1, 4, 4)

    def loop_principal(self):
        run = True

        while(run):
            self.clock.tick(self.FPS)

            self.banheiro.fill(self.fundo)

            self.banheiro.blit(self.chao, self.chao_rect.topleft)
            self.holly.desenha(self.banheiro)

            print('b',self.holly.rect.bottom)
            print('l',self.holly.rect.left)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False  # saida
                    if event.key == pygame.K_e:
                        if self.holly.rect.bottom  >= 540 and self.holly.rect.left > 110 and self.holly.rect.left < 160:
                            self.saiu = True
                            run = False
                    if event.key == pygame.K_a:
                        self.movimento_esquerda = True

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
                        self.movimento_direita = False
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
            if self.holly.rect.y <= 215:
                self.movimento_up = False

            self.holly.movimento(self.movimento_esquerda, self.movimento_direita, self.movimento_up, self.movimento_down)
            pygame.display.update()
    def saiuS (self):
        if self.saiu:
            return True
        else:
            return False
if __name__ == "__main__":
    sala = Banheiro()
    sala.loop_principal()



