
import pygame

from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from PPlay.collision import *
from PPlay.gameobject import *
from PPlay.mouse import *
import random

menu= Window (1280,720)
menu.set_background_color((0,0,0))
menu.set_title("mainmenu")


botaoJ = Sprite("JOGAR.png",1)
botaoJ.x= menu.width/2-botaoJ.width/2
botaoJ.y= menu.height- 450

botaoN=Sprite("nivel.png",1)
botaoN.x= menu.width/2-botaoN.width/2
botaoN.y= menu.height- 350

botaoP=Sprite("placar.png",1)
botaoP.x= menu.width/2-botaoP.width/2
botaoP.y= menu.height- 250

botaoS=Sprite("sair.png",1)
botaoS.x= menu.width/2-botaoS.width/2
botaoS.y= menu.height- 150

telaI= GameImage("SPACE INVADERS.png")

mouse= Window.get_mouse()



selectDifi=Nivel()
while(True):
    telaI.draw()
    botaoJ.draw()
    botaoN.draw()
    botaoS.draw()
    botaoP.draw()
    menu.update()


    if mouse.is_over_object(botaoJ) and mouse.is_button_pressed(1):
        from SI_jogo import SI_jogo
        jogar = SI_jogo()
        jogar.jog()

    if mouse.is_over_object(botaoN) and mouse.is_button_pressed(1):
        selectDifi.dificuldade()

    if mouse.is_over_object(botaoS) and mouse.is_button_pressed(1):
        menu.close()