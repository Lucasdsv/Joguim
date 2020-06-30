import pygame
import PPlay
from PPlay.window import*
from PPlay.animation import*
from PPlay.keyboard import*
from PPlay.gameimage import*
from PPlay.mouse import*


janela=Window(1300,800)
teclado=janela.get_keyboard()

mouse=janela.get_mouse()
mpos=mouse.get_position

teste=GameImage("teste.png")

pygame.mixer.music.load("somloco.wav")
pygame.mixer.music.play(-1)

cenario= GameImage("cena.png")

corp=Animation("idol.png", 5, loop=True)
corp.set_total_duration(634)
corp.set_position(janela.width/2-50, janela.height/2-50)

cab=Animation("cab.png", 5, loop=True)
cab.set_total_duration(634)
cab.set_position(corp.x + corp.width/5,corp.height-25)

enemy=Animation("enemy.png", 5 , loop=True)
enemy.set_total_duration(634)
enemy.set_position(180, janela.height/2-enemy.height/2)

time=0
ingame=1

while(1):

    while(ingame==1):
        time+=janela.delta_time()
        teste.x = cab.x-450
        teste.y = cab.y-150
        cab.set_position(corp.x + corp.width /10, corp.y -cab.width+5)

        if teclado.key_pressed("right"):
            corp.x+=800*janela.delta_time()
        if teclado.key_pressed("left"):
            corp.x-=800*janela.delta_time()
        if teclado.key_pressed("down"):
            corp.y+=800*janela.delta_time()
        if teclado.key_pressed("up"):
            corp.y-=800*janela.delta_time()
        if(cab.x>janela.width-cab.width):
            corp.x=janela.width-corp.width
        if(cab.x< 0):
            corp.x=1
        if(cab.y<=0):
            corp.y=cab.width+1
        if(corp.y>=janela.height-corp.height):
            corp.y-=1

        #teste pra ver quando q muda

        cenario.draw()
        janela.draw_text("Tempo " + str(int(time)), 5, 5, 16, (255, 255, 255), "Calibri", True)
        corp.draw()
        corp.update()
        cab.draw()
        cab.update()
        enemy.draw()
        enemy.update()

        janela.update()