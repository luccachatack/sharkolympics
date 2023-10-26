from PPlay.window import *


class Menu:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def openMenu(self):
        janela = Window(width=self.width, height=self.height)
        janela.set_title("SharkOlympcs")
        teclado = Window.get_keyboard()

        while True:
            janela.update()

            #tecla " ' " fecha a janela(apenas quando estiver no menu)
            if teclado.key_pressed("'"):
                janela.close()

            #muda para a tela principal do jogo
            if teclado.key_pressed("a"):
                return 1
