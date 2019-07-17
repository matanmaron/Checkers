# Project By:
#   Matan Maron
#   Yonatan Bar

import pygame
import Colors as colors
import Game as game
import Moves as moves
import Buttons as buttons

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.init()

gamedisplay = pygame.display.set_mode((640,400))
pygame.display.set_caption("chekers!")

#gloals
gameExit = False
insettings = False
lastx, lasty = -1,-1
drawNewboard = False

#code here
while not gameExit:

    for event in pygame.event.get():
        #draw screen
        gamedisplay.fill(colors.gray)
        # quit esc or x-click
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or pygame.K_ESCAPE:
                gameExit = True
        #logic
        elif game.inGame:#main game loop
            game.Drawboard(gamedisplay)
            buttons.ButtonBack(gamedisplay,colors.white)
            if not game.isOver():
                buttons.nowPlayertext(gamedisplay, game.isPlayer1)
            if game.isOver():
                buttons.GameOver(gamedisplay, game.isPlayer1)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x, y = x / game.sizeofrect, y / game.sizeofrect
                    if (x, y) == (9, 6) or (x, y) == (10, 6) or (x, y) == (11, 6):  # clicked back
                        buttons.ButtonBack(gamedisplay, colors.green)
                        pygame.display.update()
                        game.gameReset()
                        game.inGame = False
            else:
                List = moves.gameMoveHave2Eat(game.isPlayer1)
                if len(List)!=0:
                    #have 2 eat
                    game.isPlayer1 = moves.gameAnalizeHave2Eat(gamedisplay,game.isPlayer1,List, False)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    x, y = x / game.sizeofrect, y / game.sizeofrect
                    if (x, y) == (9, 6) or (x, y) == (10, 6) or (x, y) == (11, 6):  #clicked back
                        buttons.ButtonBack(gamedisplay, colors.green)
                        pygame.display.update()
                        game.gameReset()
                        game.inGame = False
                    elif (x>=0 and x<8 and y>=0 and y<8): #limit to board
                        game.isPlayer1 = moves.gameAnalizeMove(gamedisplay,game.isPlayer1, x, y)
        else:#main menu
            game.DrawPieces()
            buttons.MainMenu(gamedisplay)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                x,y = x/game.sizeofrect, y/game.sizeofrect
                if (x,y)==(9,1) or (x,y)==(10,1) or (x,y)==(11,1):#clicked start
                    buttons.ButtonStart(gamedisplay, colors.green)
                    pygame.display.update()
                    game.inGame = True
                if (x, y) == (9, 3) or (x, y) == (10, 3) or (x, y) == (11, 3):#clicked settings
                    buttons.ButtonSound(gamedisplay, colors.green)
                    pygame.display.update()
                    game.soundOn = not game.soundOn
                if (x, y) == (9, 6) or (x, y) == (10, 6) or (x, y) == (11, 6):#clicked exit
                    buttons.ButtonExit(gamedisplay,colors.green)
                    pygame.display.update()
                    gameExit = True
        #screen update
        pygame.display.update()


pygame.quit()
quit()
