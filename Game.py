import pygame
import Colors as colors
import numpy as np

# -1 = illegal spot
# 0 = empty cell
# 1 = player1 peon
# 2 = player2 peon
# 3 = highlight empty
# 11 = player1 highlight peon
# 12 = player1 highlight king
# 21 = player2 highlight peon
# 22 = player2 highlight king
#10 = player1 king
#20 = player2 king

#constants
sizeofrect = 50
color1 = colors.offwhite
color2 = colors.olive
colorhigh = colors.green
board = np.zeros((10,10))
visualboard = np.zeros((10,10))
isPlayer1 = True
winPlayer1 = True
inGame = False
soundOn = True

def Drawboard(gamedisplay):
    gamedisplay.fill(color1, rect=[0,0, sizeofrect*8, sizeofrect*8])
    for row in range(1,10):
        for col in range(1, 10):
            x=(row-1)*sizeofrect
            y=(col-1)*sizeofrect
            if visualboard[row,col]==0:
                gamedisplay.fill(color2, rect=[x, y, sizeofrect, sizeofrect])
            if visualboard[row, col] == 3:
                gamedisplay.fill(colorhigh, rect=[x, y, sizeofrect, sizeofrect])
            if visualboard[row,col]==1:
                gamedisplay.fill(color2, rect=[x, y, sizeofrect, sizeofrect])
                pygame.draw.circle(gamedisplay, colors.player1color,
                                   (x + sizeofrect / 2, y + sizeofrect / 2),sizeofrect / 2)
            if visualboard[row,col]==11:
                gamedisplay.fill(colorhigh, rect=[x, y, sizeofrect, sizeofrect])
                pygame.draw.circle(gamedisplay, colors.player1color,
                                   (x + sizeofrect / 2, y + sizeofrect / 2),sizeofrect / 2)
            if visualboard[row, col] == 2:
                gamedisplay.fill(color2, rect=[x, y, sizeofrect, sizeofrect])
                pygame.draw.circle(gamedisplay, colors.player2color,
                                   (x + sizeofrect / 2, y + sizeofrect / 2),sizeofrect / 2)
            if visualboard[row, col] == 21:
                gamedisplay.fill(colorhigh, rect=[x, y, sizeofrect, sizeofrect])
                pygame.draw.circle(gamedisplay, colors.player2color,
                                   (x + sizeofrect / 2, y + sizeofrect / 2),sizeofrect / 2)
            if visualboard[row, col] == 10:
                gamedisplay.fill(color2, rect=[x, y, sizeofrect, sizeofrect])
                pygame.draw.circle(gamedisplay, colors.player1color,
                                   (x + sizeofrect / 2, y + sizeofrect / 2),sizeofrect / 2)
                pygame.draw.circle(gamedisplay, colors.gold,
                                   (x + sizeofrect / 2, y + sizeofrect / 2), sizeofrect / 4)
            if visualboard[row, col] == 12:
                gamedisplay.fill(colorhigh, rect=[x, y, sizeofrect, sizeofrect])
                pygame.draw.circle(gamedisplay, colors.player1color,
                                   (x + sizeofrect / 2, y + sizeofrect / 2),sizeofrect / 2)
                pygame.draw.circle(gamedisplay, colors.gold,
                                   (x + sizeofrect / 2, y + sizeofrect / 2), sizeofrect / 4)
            if visualboard[row, col] == 20:
                gamedisplay.fill(color2, rect=[x, y, sizeofrect, sizeofrect])
                pygame.draw.circle(gamedisplay, colors.player2color,
                                   (x + sizeofrect / 2, y + sizeofrect / 2), sizeofrect / 2)
                pygame.draw.circle(gamedisplay, colors.gold,
                                   (x + sizeofrect / 2, y + sizeofrect / 2), sizeofrect / 4)
            if visualboard[row, col] == 22:
                gamedisplay.fill(colorhigh, rect=[x, y, sizeofrect, sizeofrect])
                pygame.draw.circle(gamedisplay, colors.player2color,
                                   (x + sizeofrect / 2, y + sizeofrect / 2), sizeofrect / 2)
                pygame.draw.circle(gamedisplay, colors.gold,
                                   (x + sizeofrect / 2, y + sizeofrect / 2), sizeofrect / 4)

def DrawPieces():
    board[0:10:9] = -1 #bounds
    board[:,0:10:9] = -1  # bounds
    board[1:9:2,1:9:2] = -1 #iligel spots
    board[0:10:2, 0:10:2] = -1 #iligel spots
    getWhite()
    getBlack()
    visualboard[:] = board[:]

def getWhite():
    board[2:9:2,1:4:2] = 1 #line 1 and 3
    board[1:8:2,2] = 1 #line 2

def getBlack():
    board[2:9:2, 7] = 2  # line 6 and 8
    board[1:8:2, 6:9:2] = 2  # line 7

def HighlightEmptyMoves(List):
    List2 = List[:]
    while len(List2) != 0:
        x,y,nextX,nextY = List2.pop()
        visualboard[nextX,nextY]=3

def gameReset():
    global isPlayer1
    board[:] = 0
    visualboard[:] = 0
    isPlayer1 = True

def KingsEverywhere():
    board[:, 8][board[:, 8] == 1] = 10
    board[:, 1][board[:, 1] == 2] = 20

def isOver():
    global winPlayer1
    if (np.sum(board[:] == 1)==0) and (np.sum(board[:] == 10)==0):
        winPlayer1 = False
        return True
    if (np.sum(board[:] == 2) == 0) and (np.sum(board[:] == 20) == 0):
        winPlayer1 = True
        return True
    return False