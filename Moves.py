import Game as game
import Colors as colors
import pygame
import Buttons as buttons

def ckEatUpDown(MoveDown, otherPlayer,otherKing, List, x,y ,AllDirection):
    if AllDirection:
        if game.board[x-1,y+1]==otherPlayer or game.board[x-1,y+1]==otherKing:
            if game.board[x-2,y+2]==0:
                List.append((x,y,x-2,y+2))
        if game.board[x+1,y+1]==otherPlayer or game.board[x+1,y+1]==otherKing:
            if game.board[x+2,y+2]==0:
                List.append((x,y,x+2,y+2))
        if game.board[x-1,y-1]==otherPlayer or game.board[x-1,y-1]==otherKing:
            if game.board[x-2,y-2]==0:
                List.append((x,y,x-2,y-2))
        if game.board[x+1,y-1]==otherPlayer or game.board[x+1,y-1]==otherKing:
            if game.board[x+2,y-2]==0:
                List.append((x,y,x+2,y-2))
    elif MoveDown:
        if game.board[x-1,y+1]==otherPlayer or game.board[x-1,y+1]==otherKing:
            if game.board[x-2,y+2]==0:
                List.append((x,y,x-2,y+2))
        if game.board[x+1,y+1]==otherPlayer or game.board[x+1,y+1]==otherKing:
            if game.board[x+2,y+2]==0:
                List.append((x,y,x+2,y+2))
    else:
        if game.board[x-1,y-1]==otherPlayer or game.board[x-1,y-1]==otherKing:
            if game.board[x-2,y-2]==0:
                List.append((x,y,x-2,y-2))
        if game.board[x+1,y-1]==otherPlayer or game.board[x+1,y-1]==otherKing:
            if game.board[x+2,y-2]==0:
                List.append((x,y,x+2,y-2))
    return List

def ckMoveUpDown(MoveDown, otherPlayer,otherKing, List, x,y ,AllDirection):
    if AllDirection:
        if game.board[x-1,y+1]==0:
            List.append ((x,y,x-1,y+1))
        if game.board[x+1,y+1]==0:
            List.append ((x,y,x+1,y+1))
        if game.board[x-1,y-1]==0:
            List.append ((x,y,x-1,y-1))
        if game.board[x+1,y-1]==0:
            List.append ((x,y,x+1,y-1))
    elif MoveDown:
        if game.board[x-1,y+1]==0:
            List.append ((x,y,x-1,y+1))
        if game.board[x+1,y+1]==0:
            List.append ((x,y,x+1,y+1))
    else:
        if game.board[x-1,y-1]==0:
            List.append ((x,y,x-1,y-1))
        if game.board[x+1,y-1]==0:
            List.append ((x,y,x+1,y-1))
    return List

def gameAnalizeMove(gamedisplay,isPlayer1, curX, curY):
    if isPlayer1:
        curPlayer = 1
        curPeonHigh = 11
        curKing = 10
        curKignHigh = 12
    else:
        curPlayer = 2
        curPeonHigh = 21
        curKing = 20
        curKignHigh = 22
    isKing = False
    curX += 1
    curY += 1
    if LegalChoice(curX,curY,isPlayer1):
        if game.board[curX,curY]==curPlayer or game.board[curX,curY]==curKing:
            if game.board[curX,curY] == curPlayer:
                game.visualboard[curX,curY] = curPeonHigh
            if game.board[curX,curY]==curKing:
                game.visualboard[curX,curY] = curKignHigh
                isKing = True
            moveList = getMoveOnCur(gamedisplay,isPlayer1,curX,curY)
            game.HighlightEmptyMoves(moveList)
            game.Drawboard(gamedisplay)
            buttons.ButtonBack(gamedisplay, colors.white)
            buttons.nowPlayertext(gamedisplay, game.isPlayer1)
            pygame.display.update()
            while (True):
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            nextX, nextY = pygame.mouse.get_pos()
                            nextX, nextY = nextX / game.sizeofrect, nextY / game.sizeofrect
                            if (nextX, nextY) == (9, 6) or (nextX, nextY) == (10, 6) or (nextX, nextY) == (11, 6):  # clicked back
                                buttons.ButtonBack(gamedisplay, colors.green)
                                pygame.display.update()
                                game.gameReset()
                                game.inGame = False
                                return
                            elif (nextX>=0 and nextX<8 and nextY>=0 and nextY<8): #limit to board
                                game.Drawboard(gamedisplay)
                                buttons.ButtonBack(gamedisplay, colors.white)
                                buttons.nowPlayertext(gamedisplay, game.isPlayer1)
                                # screen update
                                pygame.display.update()
                                nextX+=1
                                nextY+=1
                                if (nextX,nextY) == (curX,curY):
                                    game.visualboard[:] = game.board[:]
                                    return isPlayer1
                                elif CanMove(curX,curY,nextX,nextY,isPlayer1, isKing):
                                    Move(curX,curY,nextX,nextY,isPlayer1)
                                    game.visualboard[:] = game.board[:]
                                    return not isPlayer1
                                elif CanEat(curX,curY,nextX,nextY,isPlayer1,isKing):
                                    Eat(curX,curY,nextX,nextY,isPlayer1)
                                    game.visualboard[:] = game.board[:]
                                    List = gameMoveHave2Eat(game.isPlayer1)
                                    if len(List) != 0:
                                        # have 2 eat
                                        game.isPlayer1 = gameAnalizeHave2Eat(gamedisplay, game.isPlayer1, List, True)
                                    else:
                                        return not isPlayer1
                                else:
                                    game.visualboard[:] = game.board[:]
                                    return isPlayer1
    else:
        game.visualboard[:] = game.board[:]
        return  isPlayer1

def Move(curX,curY,x,y,isPlayer1):
    if game.soundOn:
        MoveSound = pygame.mixer.Sound("move.wav")
        pygame.mixer.Sound.play(MoveSound)
    if isPlayer1:
        curPlayer = 1
        curKing = 10
    else:
        curPlayer = 2
        curKing = 20

    if game.board[curX,curY] == curPlayer:
        cur=curPlayer
    elif game.board[curX,curY] == curKing:
        cur = curKing
    else:
        print "got problem..."
        return False
    if (x-1,y+1) == (curX,curY):
        game.board[curX,curY] = 0
        game.board[x, y] = cur
    elif (x+1,y+1) == (curX,curY):
        game.board[curX, curY] = 0
        game.board[x, y] = cur
    elif (x - 1, y - 1) == (curX, curY):
        game.board[curX, curY] = 0
        game.board[x, y] = cur
    elif (x + 1, y - 1) == (curX, curY):
        game.board[curX, curY] = 0
        game.board[x, y] = cur
    game.KingsEverywhere()

def Eat(srcX,srcY,destX,destY,isPlayer1):
    if game.soundOn:
        EatSound = pygame.mixer.Sound("eat.wav")
        pygame.mixer.Sound.play(EatSound)
    if isPlayer1:
        curPlayer = 1
        curKing = 10
    else:
        curPlayer = 2
        curKing = 20

    if game.board[srcX,srcY] == curPlayer:
        cur=curPlayer
    elif game.board[srcX,srcY] == curKing:
        cur = curKing
    else:
        print "got problem..."
        return False
    if (srcX-2,srcY+2) == (destX,destY):
        game.board[srcX,srcY] = 0
        game.board[srcX-1,srcY+1] = 0
        game.board[destX, destY] = cur
    elif (srcX+2,srcY+2) == (destX,destY):
        game.board[srcX, srcY] = 0
        game.board[srcX + 1, srcY + 1] = 0
        game.board[destX, destY] = cur
    elif (srcX - 2, srcY - 2) == (destX, destY):
        game.board[srcX, srcY] = 0
        game.board[srcX - 1, srcY - 1] = 0
        game.board[destX, destY] = cur
    elif (srcX + 2, srcY - 2) == (destX, destY):
        game.board[srcX, srcY] = 0
        game.board[srcX + 1, srcY - 1] = 0
        game.board[destX, destY] = cur
    game.KingsEverywhere()

def CanMove(curX,curY,x,y,isPlayer1, AllDirections):
    canMove = False
    if isPlayer1:
        moveDown = True
    else:
        moveDown = False
    if AllDirections:
        if (curX - 1, curY + 1) == (x, y):
            if game.board[x, y] == 0:
                game.visualboard[x,y] = 3
                canMove = True
        elif (curX + 1, curY + 1) == (x, y):
            if game.board[x, y] == 0:
                game.visualboard[x, y] = 3
                canMove = True
        if (curX - 1, curY - 1) == (x, y):
            if game.board[x, y] == 0:
                game.visualboard[x, y] = 3
                canMove = True
        elif (curX + 1, curY - 1) == (x, y):
            if game.board[x, y] == 0:
                game.visualboard[x, y] = 3
                canMove = True
    elif moveDown:
        if (curX - 1, curY + 1) == (x, y):
            if game.board[x, y] == 0:
                game.visualboard[x,y] = 3
                canMove = True
        elif (curX + 1, curY + 1) == (x, y):
            if game.board[x, y] == 0:
                game.visualboard[x, y] = 3
                canMove = True
    else:
        if (curX - 1, curY - 1) == (x, y):
            if game.board[x, y] == 0:
                game.visualboard[x, y] = 3
                canMove = True
        elif (curX + 1, curY - 1) == (x, y):
            if game.board[x, y] == 0:
                game.visualboard[x, y] = 3
                canMove = True
    return canMove

def CanEat(curX,curY,x,y,isPlayer1, AllDirections):
    if isPlayer1:
        otherPlayer = 2
        otherKing = 20
        moveDown = True
    else:
        otherPlayer = 1
        otherKing = 10
        moveDown = False
    if AllDirections:
        if (x - 2, y + 2) == (curX, curY):
            if game.board[x, y] == 0:
                if game.board[curX - 1, curY + 1] == otherPlayer or game.board[curX - 1, curY + 1] == otherKing:
                    return True
        elif (x + 2, y + 2) == (curX, curY):
            if game.board[x, y] == 0:
                if game.board[curX + 1, curY + 1] == otherPlayer or game.board[curX + 1, curY + 1] == otherKing:
                    return True
        if (x - 2, y - 2) == (curX, curY):
            if game.board[x, y] == 0:
                if game.board[curX - 1, curY - 1] == otherPlayer or game.board[curX - 1, curY - 1] == otherKing:
                    return True
        elif (x + 2, y - 2) == (curX, curY):
            if game.board[x, y] == 0:
                if game.board[curX + 1, curY - 1] == otherPlayer or game.board[curX + 1, curY - 1] == otherKing:
                    return True
    else:
        if moveDown:
            if (x - 2, y + 2) == (curX, curY):
                if game.board[x, y] == 0:
                    if game.board[curX - 1, curY + 1] == otherPlayer or game.board[curX - 1, curY + 1] == otherKing:
                        return True
            elif (x + 2, y + 2) == (curX, curY):
                if game.board[x, y] == 0:
                    if game.board[curX + 1, curY + 1] == otherPlayer or game.board[curX + 1, curY + 1] == otherKing:
                        return True
        else:
            if (x - 2, y - 2) == (curX, curY):
                if game.board[x, y] == 0:
                    if game.board[curX - 1, curY - 1] == otherPlayer or game.board[curX - 1, curY - 1] == otherKing:
                        return True
            elif (x + 2, y - 2) == (curX, curY):
                if game.board[x, y] == 0:
                    if game.board[curX + 1, curY - 1] == otherPlayer or game.board[curX + 1, curY - 1] == otherKing:
                        return True
    return False

def LegalChoice(x,y,isPlayer1):
    if isPlayer1:
        otherPlayer = 2
        otherKing = 20
        moveDown = True
        curPlayer = 1
        curKing = 10
    else:
        otherPlayer = 1
        otherKing = 10
        moveDown = False
        curPlayer = 2
        curKing = 20
    isKing = False
    if game.board[x, y] == curKing:
        isKing = True
    if isKing:
        if game.board[x - 1, y + 1] == 0 or game.board[x + 1, y + 1] == 0:
            return True
        if game.board[x - 1, y + 1] == otherPlayer or game.board[x - 1, y + 1] == otherKing:
            if game.board[x - 2, y + 2] == 0:
                return True
        if game.board[x + 1, y + 1] == otherPlayer or game.board[x + 1, y + 1] == otherKing:
            if game.board[x + 2, y + 2] == 0:
                return True
        if game.board[x - 1, y - 1] == 0 or game.board[x + 1, y - 1] == 0:
            return True
        if game.board[x - 1, y - 1] == otherPlayer or game.board[x - 1, y - 1] == otherKing:
            if game.board[x - 2, y - 2] == 0:
                return True
        if game.board[x + 1, y - 1] == otherPlayer or game.board[x + 1, y - 1] == otherKing:
            if game.board[x + 2, y - 2] == 0:
                return True
    elif game.board[x, y] == curPlayer:
        if moveDown:
            if game.board[x - 1, y + 1] == 0 or game.board[x + 1, y + 1] == 0:
                return True
            if game.board[x - 1, y + 1]== otherPlayer or game.board[x - 1, y + 1]== otherKing:
                if game.board[x - 2, y + 2] == 0:
                    return True
            if game.board[x + 1, y + 1]== otherPlayer or game.board[x + 1, y + 1]== otherKing:
                if game.board[x + 2, y + 2] == 0:
                    return True
        else:
            if game.board[x - 1, y - 1] == 0 or game.board[x + 1, y - 1] == 0:
                return True
            if game.board[x - 1, y - 1]== otherPlayer or game.board[x - 1, y - 1]== otherKing:
                if game.board[x - 2, y - 2] == 0:
                    return True
            if game.board[x + 1, y - 1]== otherPlayer or game.board[x + 1, y - 1]==otherKing:
                if game.board[x + 2, y - 2] == 0:
                    return True
    return False

def getMoveOnCur(gamedisplay,isPlayer1,x,y):
    haveList = []
    if isPlayer1:
        curPlayer = 1
        curKing = 10
        otherPlayer = 2
        otherKing = 20
        moveDown = True
    else:
        curPlayer = 2
        curKing = 20
        otherPlayer = 1
        otherKing = 10
        moveDown = False
    if game.board[x, y] == curPlayer:
        haveList = ckMoveUpDown(moveDown, otherPlayer, otherKing, haveList, x, y,False)
    elif game.board[x, y] == curKing:
        haveList = ckMoveUpDown(not moveDown, otherPlayer, otherKing, haveList, x, y,True)
    else:
        print "got problem..."
        return
    return haveList

def gameMoveHave2Eat(isPlayer1):
    haveList = []
    if isPlayer1:
        curPlayer = 1
        curKing = 10
        otherPlayer = 2
        otherKing = 20
        moveDown = True
    else:
        curPlayer = 2
        curKing = 20
        otherPlayer = 1
        otherKing = 10
        moveDown = False
    for x in range(1, 9):
        for y in range(1, 9):
            if game.board[x, y] == curPlayer:
                haveList = ckEatUpDown(moveDown,otherPlayer, otherKing,haveList,x,y, False)
            elif game.board[x, y] == curKing:
                haveList = ckEatUpDown(moveDown, otherPlayer, otherKing, haveList, x, y, True)
    return haveList

def GameSecondEat(isPlayer1,x,y):
    haveList = []
    if isPlayer1:
        otherPlayer = 2
        otherKing = 20
        moveDown = True
    else:
        otherPlayer = 1
        otherKing = 10
        moveDown = False
    haveList = ckEatUpDown(moveDown, otherPlayer, otherKing, haveList, x, y, True)
    return haveList

def gameAnalizeHave2Eat(gamedisplay,isPlayer1,List, isSecondMove):
    game.HighlightEmptyMoves(List)
    if isPlayer1:
        curPlayer = 1
        curPeonHigh = 11
        curKing = 10
        curKignHigh = 12
    else:
        curPlayer = 2
        curPeonHigh = 21
        curKing = 20
        curKignHigh = 22

    game.Drawboard(gamedisplay)
    buttons.ButtonBack(gamedisplay, colors.white)
    buttons.nowPlayertext(gamedisplay, game.isPlayer1)
    # screen update
    pygame.display.update()
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                x, y = x / game.sizeofrect, y / game.sizeofrect
                if (x, y) == (9, 6) or (x, y) == (10, 6) or (x, y) == (11, 6):  # clicked back
                    buttons.ButtonBack(gamedisplay, colors.green)
                    pygame.display.update()
                    game.gameReset()
                    game.inGame = False
                    return
                elif (x >= 0 and x < 8 and y >= 0 and y < 8):  # limit to board
                    x += 1
                    y += 1
                    List2 = List[:]
                    while len(List2) != 0:
                        srcX, srcY, destX, destY = List2.pop()
                        if (srcX,srcY) == (x, y):
                            if game.board[x, y] == curPlayer:
                                game.visualboard[x, y] = curPeonHigh
                            if game.board[x, y] == curKing:
                                game.visualboard[x, y] = curKignHigh
                            game.Drawboard(gamedisplay)
                            buttons.ButtonBack(gamedisplay, colors.white)
                            buttons.nowPlayertext(gamedisplay, game.isPlayer1)
                            # screen update
                            pygame.display.update()
                            while (True):
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        nextX, nextY = pygame.mouse.get_pos()
                                        nextX, nextY = nextX / game.sizeofrect, nextY / game.sizeofrect
                                        if (nextX, nextY) == (9, 6) or (nextX, nextY) == (10, 6) or (nextX, nextY) == (
                                                11, 6):  # clicked back
                                            buttons.ButtonBack(gamedisplay, colors.green)
                                            pygame.display.update()
                                            game.gameReset()
                                            game.inGame = False
                                            return
                                        elif (nextX >= 0 and nextX < 8 and nextY >= 0 and nextY < 8):  # limit to board
                                            game.Drawboard(gamedisplay)
                                            buttons.ButtonBack(gamedisplay, colors.white)
                                            buttons.nowPlayertext(gamedisplay, game.isPlayer1)
                                            # screen update
                                            pygame.display.update()
                                            nextX += 1
                                            nextY += 1
                                            if (x,y) == (nextX,nextY):
                                                game.visualboard[:] = game.board[:]
                                                return isPlayer1
                                            if (nextX, nextY) == (destX, destY):
                                                Eat(x, y, nextX, nextY, isPlayer1)
                                                game.visualboard[:] = game.board[:]
                                                newList = GameSecondEat(isPlayer1,nextX,nextY)
                                                if len(newList) != 0:
                                                    # have 2 eat AGAIN !
                                                    gameAnalizeHave2Eat(gamedisplay,isPlayer1,newList,True)
                                                return not isPlayer1