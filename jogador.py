import os
import pygame
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.gameobject import *
from PPlay.mouse import *
import random
from pathlib import Path
pygame.init()

class Holly(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, velocidade,velocidadey):
        pygame.sprite.Sprite.__init__(self)

        self.velocidade = velocidade
        self.velocidadey = velocidadey
        self.velocidade_original = velocidade
        self.velocidadey_original = velocidadey
        self.direcao = 'down'
        self.mover_para_baixo = False
        self.mover_para_cima= False
        self.animacoes = {'left': [], 'right': [], 'up': [], 'down': []}

        self.frame_index = 0
        self.atualizar_tempo = pygame.time.get_ticks()
        self.animacao_fresh = 250

        for j in range(4):
            img = pygame.image.load(f'C:/Users/maisa/OneDrive/Desktop/hollys escape/imgholly/{j}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animacoes['down'].append(img)

        for j in range(4):
            img = pygame.image.load(f'C:/Users/maisa/OneDrive/Desktop/hollys escape/imghollyE/{j}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animacoes['left'].append(img)

        for j in range(4):
            img = pygame.image.load(f'C:/Users/maisa/OneDrive/Desktop/hollys escape/imghollyD/{j}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animacoes['right'].append(img)

        for j in range(4):
            img = pygame.image.load(f'C:/Users/maisa/OneDrive/Desktop/hollys escape/imghollyU/{j}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.animacoes['up'].append(img)

        self.image = self.animacoes[self.direcao][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def movimento(self, mov_esq, mov_dir, mov_up, mov_dow):
        dx = 0
        dy = 0

        movendo = False
        if mov_esq:
            dx = -self.velocidade
            self.direcao = 'left'
            movendo = True
        if mov_dir:
            dx = self.velocidade
            self.direcao = 'right'
            movendo = True

        if mov_up:
            dy = -self.velocidadey
            self.direcao = 'up'
            movendo = True

        if mov_dow:
            dy = self.velocidadey
            self.direcao = 'down'
            movendo = True
            self.mover_para_baixo = True
        # Atualiza retângulos da imagem e posição
        self.rect.x += dx
        self.rect.y += dy
        if movendo:
            self.atualizar_animacao()
        else:
            self.frame_index = 0
            self.image = self.animacoes[self.direcao][self.frame_index]


    def atualizar_animacao(self):
        # Verifica se é hora de atualizar a animação
        if pygame.time.get_ticks() - self.atualizar_tempo > self.animacao_fresh:
            self.atualizar_tempo = pygame.time.get_ticks()
            self.frame_index += 1

            # Se chegamos ao fim da lista de animação, reinicia o índice
            if self.frame_index >= len(self.animacoes[self.direcao]):
                self.frame_index = 0

        # Atualiza a imagem atual
        self.image = self.animacoes[self.direcao][self.frame_index]
    def colidiu(self,objeto):
        colidiu = False
        if objeto.left< self.rect.centerx< objeto.right and objeto.top < self.rect.centery< objeto.bottom:
            colidiu = True
        return colidiu
    def colisaoB(self, objeto):
        colidiu = False
        if objeto.top <= self.rect.bottom <= objeto.bottom and self.rect.left > objeto.left and self.rect.right < objeto.right:
            colidiu = True
        return colidiu

    def colisaoC(self, objeto):
        colidiu = False
        if objeto.bottom >= self.rect.bottom >= objeto.top and self.rect.right > objeto.left and self.rect.left < objeto.right:
            colidiu = True
        return colidiu

    def colisaoE(self, objeto):
        colidiu = False
        if objeto.left <= self.rect.left <= objeto.right and self.rect.bottom > objeto.top and self.rect.bottom < objeto.bottom:
            colidiu = True
        return colidiu

    def colisaoD(self,objeto):
        colidiu = False
        if objeto.right >= self.rect.right >= objeto.left and self.rect.bottom > objeto.top and self.rect.bottom < objeto.bottom:
            colidiu = True

        return colidiu
        #def colisaoE():

        #def colisaoD
        #def colisaoU
    def onde_estou(self):
        return self.rect
    def desenha(self, jogo):
        jogo.blit(self.image, self.rect)
