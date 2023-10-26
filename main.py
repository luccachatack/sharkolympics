from jogo import Jogo
from menu import Menu


width = 500
height = 300

gamestate = 0
while True:

    #criar um if gamestate==0 para o menu
    if gamestate == 0:
        menu = Menu(width, height)
        menu.openMenu()
        gamestate = menu.openMenu()

        print(gamestate)

    #para rodar o jogo principal(1)
    if gamestate==1:
        game = Jogo(width, height)
        game.jogo()

        gamestate = game.jogo()
        print(gamestate)

