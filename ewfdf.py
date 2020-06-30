from PPlay.mouse import*
from PPlay.window import*

janela=Window(1300,800)
mouse=janela.get_mouse()

teste=mouse.get_position()

print(teste[0])