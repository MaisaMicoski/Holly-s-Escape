import pygame

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.gameobject import *
from PPlay.mouse import *
import random

class colisao:
    def __init__(self, obj1, obj2):
        self.cima = False
        self.ladoE = False
        self.ladoD = False
        self.baixo = False

        def colidiu(obj1, obj2):
            if obj1.collided(obj2):
