import pygame

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.gameobject import *
from PPlay.mouse import *
import random

from banheiro import Banheiro
from camera import CameraGroup
from jogador import *
from sala1 import Sala1
from sala2 import Sala2

class Corredor:
    def __init__(self):
        pygame.init()
        self.saiuSala1 = False
        self.jogo = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('jogo')

        self.clock = pygame.time.Clock()
        self. FPS = 60
        self. parede = pygame.image.load('parede1.png')
        self. parede = pygame.transform.scale(self.parede, (int(self.parede.get_width() * 1.2), int(self.parede.get_height() *1.25)))
        self.parede_rect = self.parede.get_rect()
        self. parede_rect.bottom = self.jogo.get_height()/2
        self.parede_rect.topleft = (0, 120)

        self.fundo = pygame.Color('black')
        self.porta1 = pygame.image.load('porta1.png')
        self.porta1 = pygame.transform.scale(self.porta1, (int(self.porta1.get_width()*1.215), int (self.porta1.get_height()*1.215)))
        self. porta1_rect = self.porta1.get_rect()
        self.porta1_rect.bottom = self.jogo.get_height()/2
        self.porta1_rect.topleft = (473, 134)

        self.porta2 = pygame.image.load('porta1.png')
        self.porta2 = pygame.transform.scale(self.porta2, (int(self.porta2.get_width()*1.215), int (self.porta2.get_height()*1.215)))
        self.porta2_rect = self.porta2.get_rect()
        self.porta2_rect.bottom = self.jogo.get_height()/2
        self.porta2_rect.topleft = (975, 134)

        self.porta3 = pygame.image.load('porta3.png')
        self.porta3 = pygame.transform.scale(self.porta3, (int(self.porta3.get_width()*1.215), int (self.porta3.get_height()*1.215)))
        self.porta3_rect = self.porta3.get_rect()
        self.porta3_rect.bottom = self.jogo.get_height()/2
        self.porta3_rect.topleft = (1418, 134)

        self.chao = pygame.image.load("chao.png")
        self.chao = pygame.transform.scale(self.chao, (int(self.chao.get_width() * 1.2), int(self.chao.get_height() * 1.2)))
        self.chao_rect = self.chao.get_rect()
        self.chao_rect.bottom = self.jogo.get_height()/2-self.chao.get_height()+1000
        self.chao_rect.topleft = (0, 60)
        #teclado = Window.get_keyboard()
        self.vel = 7
        self.velH = 1
        self.holly = Holly(200,260,1, 3, 4)
        self.velp=1
        self.run = True
        self.movimento_esquerda = False
        self.movimento_direita = False
        self.movimento_up = False
        self.movimento_down = False

        self.sprint = 100

        self.camera = CameraGroup()
        self.sala1 = False
        self.banheiro1 = False
        self.sala2 = False

        self.apertandoE = False
    def sala_atual(self, nova_sala):
        aux = nova_sala
        aux.loop_principal()

    def loop_principal(self):
        run = True

        while(run):

            self.clock.tick(self.FPS)
            self. jogo.fill(self.fundo)
            self.jogo.blit(self.chao, self.chao_rect.topleft)
            self. jogo.blit(self.parede, self.parede_rect.topleft)
            self.jogo.blit(self.porta1, self.porta1_rect.topleft)
            self.jogo.blit(self.porta2, self.porta2_rect.topleft)
            self.jogo.blit(self.porta3,self. porta3_rect.topleft)

            self.holly.desenha(self.jogo)

            #if holly.rect.bottom >= parede_rect.bottom:

            #if holly_rect.bottom <= parede_rect.bottom:

            #camera.center_target_camera(holly)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                #movimentos

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False  # saida
                    if event.key == pygame.K_e:
                        if self.holly.colidiu(self.porta1_rect):
                            self.sala_atual(Sala1())
                        if self.holly.colidiu(self.porta2_rect):
                            self.sala_atual(Sala2())
                        if self.holly.colidiu(self.porta3_rect):
                            self.sala_atual(Banheiro())

                    if event.key == pygame.K_a:
                        self.movimento_esquerda = True

                    if event.key == pygame.K_d:
                        self.movimento_direita = True

                    if event.key == pygame.K_w:
                        self. movimento_up = True
                    if event.key == pygame.K_s:
                        self.movimento_down = True
                    if event.key == pygame.K_LSHIFT:
                        while self.sprint > 0:
                            vel = 100
                            self.sprint -= 1

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movimento_esquerda = False
                    if event.key == pygame.K_d:
                        self.movimento_direita = False
                    if event.key == pygame.K_w:
                        self.movimento_up = False
                    if event.key == pygame.K_s:
                        self.movimento_down = False
                    if event.key == pygame.K_LSHIFT:
                        self.sprint += 1

                self.holly_rect = self.holly.onde_estou()

                # Movimento à esquerda
                if self.movimento_esquerda:
                    if self.holly_rect.left > 50 and self.chao_rect.left < 0:
                        self.parede_rect.x += self.vel
                        self.chao_rect.x += self.vel
                        self.porta1_rect.x += self.vel
                        self.porta2_rect.x += self.vel
                        self.porta3_rect.x += self.vel
                # Movimento à direita
                if self.movimento_direita:
                    if self.holly_rect.right < self.jogo.get_width() - 50 and self.chao_rect.right > self.jogo.get_width():
                        self.parede_rect.x -= self.vel
                        self.chao_rect.x -= self.vel
                        self.porta1_rect.x -= self.vel
                        self.porta2_rect.x -= self.vel
                        self.porta3_rect.x -= self.vel
            if self.holly.colisaoB(self.parede_rect):
                self.movimento_up = False
            if self.holly_rect.bottom >= self.chao_rect.bottom:
                self.movimento_down = False
            self.holly.movimento(self.movimento_esquerda, self.movimento_direita,self. movimento_up, self.movimento_down)


            if self.sprint > 100:
                self.sprint = 100

            pygame.display.update()

def main():
    # Inicializa o jogo
    corredor = Corredor()
    corredor.loop_principal()


if __name__ == "__main__":
    main()