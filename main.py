# Project By:
#   Matan Maron
#   Yonatan Bar

import pygame
import Colors as colors
import Game as game
import Moves as moves
import Buttons as buttons
import sys
import os

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.init()

# Helper to load resources correctly in PyInstaller --onefile
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Override sound loading in Game module
game.MoveSoundPath = resource_path("move.wav")
game.EatSoundPath = resource_path("eat.wav")

gamedisplay = pygame.display.set_mode((640,400))
pygame.display.set_caption("chekers!")

# globals
gameExit = False
insettings = False
lastx, lasty = -1,-1
drawNewboard = False

# code here
while not gameExit:

    for event in pygame.event.get():
        # draw screen
        gamedisplay.fill(colors.gray)

        # quit esc or x-click
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                gameExit = True

        # handle mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x, y = x // game.sizeofrect, y // game.sizeofrect  # integer division

            if game.inGame:
                List = moves.gameMoveHave2Eat(game.isPlayer1)
                if len(List) != 0:
                    game.isPlayer1 = moves.gameAnalizeHave2Eat(gamedisplay, game.isPlayer1, List, False)
                elif 0 <= x < 8 and 0 <= y < 8:
                    game.isPlayer1 = moves.gameAnalizeMove(gamedisplay, game.isPlayer1, x, y)
                elif (x, y) in [(9, 6), (10, 6), (11, 6)]:  # clicked back
                    buttons.ButtonBack(gamedisplay, colors.green)
                    pygame.display.update()
                    game.gameReset()
                    game.inGame = False
            else:  # main menu
                if (x,y) in [(9,1),(10,1),(11,1)]:  # clicked start
                    buttons.ButtonStart(gamedisplay, colors.green)
                    pygame.display.update()
                    game.inGame = True
                elif (x,y) in [(9,3),(10,3),(11,3)]:  # clicked settings
                    buttons.ButtonSound(gamedisplay, colors.green)
                    pygame.display.update()
                    game.soundOn = not game.soundOn
                elif (x,y) in [(9,6),(10,6),(11,6)]:  # clicked exit
                    buttons.ButtonExit(gamedisplay, colors.green)
                    pygame.display.update()
                    gameExit = True

        # logic
        elif game.inGame:  # main game drawing
            game.Drawboard(gamedisplay)
            buttons.ButtonBack(gamedisplay, colors.white)
            if not game.isOver():
                buttons.nowPlayertext(gamedisplay, game.isPlayer1)
            if game.isOver():
                buttons.GameOver(gamedisplay, game.isPlayer1)

        else:  # main menu drawing
            game.DrawPieces()
            buttons.MainMenu(gamedisplay)

        # screen update
        pygame.display.update()

pygame.quit()
quit()
