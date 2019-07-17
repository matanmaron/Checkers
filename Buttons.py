import Colors as colors
import pygame
import Game as game

def DrawButton(gamedisplay, color,text, rect, center):
    smalltext = pygame.font.SysFont(None, 24)
    gamedisplay.fill(color, rect = rect)  # start
    textstart_Surf, textstart_rect = text_objects(text, smalltext, colors.black)
    textstart_rect.center = center
    gamedisplay.blit(textstart_Surf, textstart_rect)

def MainMenu(gamedisplay):
    ButtonStart(gamedisplay,colors.white)
    ButtonSound(gamedisplay,colors.white)
    ButtonExit(gamedisplay,colors.white)

def ButtonStart (gamedisplay,color):
    DrawButton(gamedisplay,color,"Start a Game!",[450, 50, 150, 50],(525, 75))

def ButtonExit (gamedisplay,color):
    DrawButton(gamedisplay,color,"Exit",[450, 300, 150, 50],(525, 325))

def ButtonSound (gamedisplay,color):
    if game.soundOn:
        text = "Sound On"
    else:
        text = "Sound Off"
    DrawButton(gamedisplay, color, text, [450, 150, 150, 50],(525, 175))

def SettingsMenu(gamedisplay):
    ButtonPlayer1color(gamedisplay,colors.white)
    ButtonPlayer2color(gamedisplay, colors.white)
    ButtonBack(gamedisplay, colors.white)

def ButtonPlayer1color(gamedisplay, color):
    DrawButton(gamedisplay, color,"Player 1 Color",[450, 50, 150, 50],(525, 75))

def ButtonPlayer2color(gamedisplay,color):
    DrawButton(gamedisplay, color,"Player 2 Color",[450, 150, 150, 50],(525, 175))

def ButtonBack (gamedisplay,color):
    DrawButton(gamedisplay, color,"Back",[450, 300, 150, 50],(525, 325))

def text_objects(tex,font,color):
    textSurface = font.render(tex,True,color)
    return textSurface, textSurface.get_rect()

def nowPlayertext(gamedisplay,isPlayer1):
    smalltext = pygame.font.SysFont(None, 24)
    if isPlayer1:
        text = "Player 1 Turn:"
        pygame.draw.circle(gamedisplay, colors.player1color,(525,125), game.sizeofrect / 2)
    else:
        text = "Player 2 Turn:"
        pygame.draw.circle(gamedisplay, colors.player2color,(525,125), game.sizeofrect / 2)
    textstart_Surf, textstart_rect = text_objects(text, smalltext, colors.black)
    textstart_rect.center = (525, 75)
    gamedisplay.blit(textstart_Surf, textstart_rect)

def GameOver(gamedisplay, isPlayer1):
    smalltext = pygame.font.SysFont(None, 24)
    bigtext = pygame.font.SysFont(None, 60,bold=True)
    textgame = "G A M E"
    textover = "O V E R"
    if game.winPlayer1:
        ptext = "Player 1 Win !"
        pygame.draw.circle(gamedisplay, colors.player1color, (525, 125), game.sizeofrect / 2)
    else:
        ptext = "Player 2 Win !"
        pygame.draw.circle(gamedisplay, colors.player2color, (525, 125), game.sizeofrect / 2)

    textstart_Surf, textstart_rect = text_objects(textgame, bigtext, colors.black)
    textstart_rect.center = (195, 180)
    gamedisplay.blit(textstart_Surf, textstart_rect)
    textstart_Surf, textstart_rect = text_objects(textover, bigtext, colors.black)
    textstart_rect.center = (200, 230)
    gamedisplay.blit(textstart_Surf, textstart_rect)

    textstart_Surf, textstart_rect = text_objects(ptext, smalltext, colors.black)
    textstart_rect.center = (525, 75)
    gamedisplay.blit(textstart_Surf, textstart_rect)