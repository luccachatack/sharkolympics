from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

class Jogo:

    #metodo construtor
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def jogo(self):

        #configuração do jogo e janela
        janela = Window(width=self.width, height=self.height)
        janela.set_title("SharkOlympcs")
        teclado = Window.get_keyboard()
        fundo = GameImage('fundo.png')

        #jogador
        jogador = GameImage('tubarao padrao.png')
        #posição inicial
        jogador.set_position(janela.width // 32, janela.height - (janela.height // 4))
        velocidade_x=1
        velocidade_y=1

        espaço= True

        #loop do jogo
        while True:
            janela.update()

            ##quando o personagem chegar na metade da tela ele vai subir e depois descer (salto)
            #subida
            if jogador.x >=janela.width - (janela.width // 2) and jogador.x <= janela.width - (janela.width // 4):
                jogador.x +=velocidade_x
                jogador.y -=velocidade_y
            #descida
            if jogador.x >= janela.width - (janela.width // 4) and jogador.x <= janela.width - (janela.width // 8   ):
                jogador.x += velocidade_x
                jogador.y += velocidade_y


            #fechar o jogo
            #tirar o janela.lose e colocá-la no menu apenas(colocar para retornar ao menu no return)
            if teclado.key_pressed("ESC"):
                return 0
            #jogador
            if teclado.key_pressed("space") and espaço== True:
                jogador.x += 8
                espaço=False

            elif teclado.key_pressed("space")==False:
                espaço= True


            if teclado.key_pressed("left"):
                jogador.x -= 5

            if teclado.key_pressed("right"):
                jogador.x += 5

            if teclado.key_pressed("up"):
                jogador.y -= 5
            elif teclado.key_pressed("down"):
                jogador.y += 5

            #Delimitando a tela
            if jogador.x <= 0:
                jogador.x = 0
            elif jogador.x >= janela.width-jogador.width:
                jogador.x = janela.width - jogador.width

            if jogador.y <= 0:
                jogador.y = 0
            elif jogador.y >= janela.height-jogador.height:
                jogador.y = janela.height - jogador.height


            #imagens
            fundo.draw()
            jogador.draw()





