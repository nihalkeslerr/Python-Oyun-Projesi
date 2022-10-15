import sqlite3
import sys
import pygame
import random
from tkinter import *
counter = 0
pygame.init()


arkaplan_rengi = (230, 239, 253, 1)
grid_rengi = (127, 92, 218, 1)

oyun_genislik = 16
oyun_yukseklik = 13
ghostsayisi = 10
sizeofgrids = 40
borderofgame = 40
borderRight=50
borderTop = 150
user = "Guest" 



ekran_en = sizeofgrids * oyun_genislik + borderofgame * 2
ekran_boy = sizeofgrids * oyun_yukseklik + borderofgame + borderTop
oyun_ekrani = pygame.display.set_mode((ekran_en, ekran_boy))
timer = pygame.time.Clock()
pygame.display.set_caption("")

yazi_tipi=pygame.font.SysFont('Arial',25)
yazi=yazi_tipi.render("OUT", True, grid_rengi)




spr_emptyGrid = pygame.image.load("Sprites/empty.png")
spr_flag = pygame.image.load("Sprites/flag.png")
spr_grid = pygame.image.load("Sprites/Grid.png")
spr_grid1 = pygame.image.load("Sprites/grid1.png")
spr_grid2 = pygame.image.load("Sprites/grid2.png")
spr_grid3 = pygame.image.load("Sprites/grid3.png")
spr_grid4 = pygame.image.load("Sprites/grid4.png")
spr_grid5 = pygame.image.load("Sprites/grid5.png")
spr_grid6 = pygame.image.load("Sprites/grid6.png")
spr_grid7 = pygame.image.load("Sprites/grid7.png")
spr_grid8 = pygame.image.load("Sprites/grid8.png")
spr_ghost = pygame.image.load("Sprites/ghost.png")
spr_ghostClicked = pygame.image.load("Sprites/ghostClicked.png")
spr_WrongGhost = pygame.image.load("Sprites/WrongGhost.png")
spr_ghosticon = pygame.image.load("Sprites/ghosticon.png")
spr_timeicon = pygame.image.load("Sprites/timeicon.png")
spr_sghosticon = pygame.image.load("Sprites/sghosticon.png")
spr_restarticon = pygame.image.load("Sprites/restart.png")
spr_backgroundicon = pygame.image.load("Sprites/background.png")
spr_wonicon = pygame.image.load("Sprites/won.png")
spr_gameovericon = pygame.image.load("Sprites/gameover.png")




grid = []
ghosts = []


connection = sqlite3.connect('database.db')
query="""SELECT * FROM login order by id DESC LIMIT 1"""
result=connection.execute(query)
for row in enumerate(result):
    temp= row[1][1]
result2 = connection.execute("""select username from gamers where mail = ? """,(temp,))
for data in enumerate(result2):
    user= data[1][0]





def YaziYaz(txt, s, yOff=0):
    text0fscreen = pygame.font.SysFont("Marker Felt", s, True).render(txt, True, (215, 128, 37,1))
    rect = text0fscreen.get_rect()
    rect.center = (oyun_genislik * sizeofgrids / 2 + borderofgame + 30, oyun_yukseklik * sizeofgrids / 2 + borderTop + yOff)
    oyun_ekrani.blit(text0fscreen, rect)

def YaziYaz2(txt, s, yOff=0):
    screen_text = pygame.font.SysFont("Marker Felt", s, True).render(txt, True, (148, 170, 217,1))
    rect = screen_text.get_rect()
    rect.center = (oyun_genislik * sizeofgrids / 2 + borderofgame + 30, oyun_yukseklik * sizeofgrids / 2 + borderTop + yOff + 10)
    oyun_ekrani.blit(screen_text, rect)

# Create class grid
class Grid:
    def __init__(self, xGrid, yGrid, type):
        self.xGrid = xGrid
        self.yGrid = yGrid
        self.clicked = False
        self.ghostClicked = False
        self.WrongGhost = False
        self.flag = False

        self.rect = pygame.Rect(borderofgame + self.xGrid * sizeofgrids, borderTop + self.yGrid * sizeofgrids, sizeofgrids, sizeofgrids)
        self.val = type

    def creategrids(self):
        if self.WrongGhost:
            oyun_ekrani.blit(spr_WrongGhost, self.rect)
        else:
            if self.clicked:
                if self.val == -1:
                    if self.ghostClicked:
                        oyun_ekrani.blit(spr_ghostClicked, self.rect)
                    else:
                        oyun_ekrani.blit(spr_ghost, self.rect)
                else:
                    if self.val == 0:
                        oyun_ekrani.blit(spr_emptyGrid, self.rect)
                    elif self.val == 1:
                        oyun_ekrani.blit(spr_grid1, self.rect)
                    elif self.val == 2:
                        oyun_ekrani.blit(spr_grid2, self.rect)
                    elif self.val == 3:
                        oyun_ekrani.blit(spr_grid3, self.rect)
                    elif self.val == 4:
                        oyun_ekrani.blit(spr_grid4, self.rect)
                    elif self.val == 5:
                        oyun_ekrani.blit(spr_grid5, self.rect)
                    elif self.val == 6:
                        oyun_ekrani.blit(spr_grid6, self.rect)
                    elif self.val == 7:
                        oyun_ekrani.blit(spr_grid7, self.rect)
                    elif self.val == 8:
                        oyun_ekrani.blit(spr_grid8, self.rect)

            else:
                if self.flag:
                    oyun_ekrani.blit(spr_flag, self.rect)
                else:
                    oyun_ekrani.blit(spr_grid, self.rect)

    def revealGrid(self):
        self.clicked = True
        if self.val == 0:
            for x in range(-1, 2):
                if self.xGrid + x >= 0 and self.xGrid + x < oyun_genislik:
                    for y in range(-1, 2):
                        if self.yGrid + y >= 0 and self.yGrid + y < oyun_yukseklik:
                            if not grid[self.yGrid + y][self.xGrid + x].clicked:
                                grid[self.yGrid + y][self.xGrid + x].revealGrid()
        elif self.val == -1:
            for m in ghosts:
                if not grid[m[1]][m[0]].clicked:
                    grid[m[1]][m[0]].revealGrid()

    def changeValue(self):
        if self.val != -1:
            for x in range(-1, 2):
                if self.xGrid + x >= 0 and self.xGrid + x < oyun_genislik:
                    for y in range(-1, 2):
                        if self.yGrid + y >= 0 and self.yGrid + y < oyun_yukseklik:
                            if grid[self.yGrid + y][self.xGrid + x].val == -1:
                                self.val += 1


def maingame():

    gameState = "Playing"
    remainingghost = ghostsayisi
    global grid
    grid = []
    global ghosts
    time = 0


    ghosts = [[random.randrange(0, oyun_genislik),
               random.randrange(0, oyun_yukseklik)]]

    for st in range(ghostsayisi - 1):
        pos = [random.randrange(0, oyun_genislik),
               random.randrange(0, oyun_yukseklik)]
        same = True
        while same:
            for i in range(len(ghosts)):
                if pos == ghosts[i]:
                    pos = [random.randrange(0, oyun_genislik), random.randrange(0, oyun_yukseklik)]
                    break
                if i == len(ghosts) - 1:
                    same = False
        ghosts.append(pos)


    for j in range(oyun_yukseklik):
        line = []
        for i in range(oyun_genislik):
            if [i, j] in ghosts:
                line.append(Grid(i, j, -1))
            else:
                line.append(Grid(i, j, 0))
        grid.append(line)


    for i in grid:
        for j in i:
            j.changeValue()


    while gameState != "Exit":

        oyun_ekrani.fill(arkaplan_rengi)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameState = "Exit"

            if gameState == "Game Over" or gameState == "Win":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gameState = "Exit"
                        maingame()
            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in grid:
                        for j in i:
                            if j.rect.collidepoint(event.pos):
                                if event.button == 1:
                                    j.revealGrid()
                                    if j.flag:
                                        remainingghost += 1
                                        j.falg = False

                                    if j.val == -1:
                                        gameState = "Game Over"
                                        j.ghostClicked = True
                                elif event.button == 3:

                                    if not j.clicked:
                                        if j.flag:
                                            j.flag = False
                                            remainingghost += 1
                                        else:
                                            j.flag = True
                                            remainingghost -= 1


        w = True
        for i in grid:
            for j in i:
                j.creategrids()
                if j.val != -1 and not j.clicked:
                    w = False
        if w and gameState != "Exit":
            gameState = "Win"


        if gameState != "Game Over" and gameState != "Win":
            time += 1
        elif gameState == "Game Over":
            oyun_ekrani.blit(spr_backgroundicon, (borderofgame + 150, borderofgame + 295))
            oyun_ekrani.blit(spr_gameovericon, (borderofgame + 160, borderofgame + 335))
            YaziYaz("Game Over!", 45)
            oyun_ekrani.blit(spr_restarticon, (borderofgame + 230, borderofgame + 405))
            YaziYaz2("R to restart", 20, 50)
            for i in grid:
                for j in i:
                    if j.flag and j.val != -1:
                        j.WrongGhost = True
        else:
            oyun_ekrani.blit(spr_backgroundicon, (borderofgame + 150, borderofgame + 295))
            oyun_ekrani.blit(spr_wonicon, (borderofgame + 160, borderofgame + 325))
            YaziYaz("You WON!", 50)
            global counter
            if counter == 0 :
                connection.execute("""UPDATE gamers SET score=score+10 WHERE gamers.mail=? """,(temp,))
                connection.commit()
                counter = counter +1
                print(temp, " kazandıı ")

            oyun_ekrani.blit(spr_restarticon, (borderofgame + 230, borderofgame + 405))
            YaziYaz2("R to restart", 20, 50)
            YaziYaz("", 50)
            YaziYaz("", 35, 150)


        s = str(time // 15)


        #UP MENU----

        text0fscreen = pygame.font.SysFont("Marker Felt", 24).render(s, True, (11, 0, 112,1))
        oyun_ekrani.blit(text0fscreen, (borderofgame + 400, borderofgame + 40)) #timerı oynatıyor bordera göre -ilk kısım:x ikinci:y
        # Draw mine left
        text0fscreen = pygame.font.SysFont("Marker Felt", 24).render(remainingghost.__str__(), True, (11, 0, 112,1))
        oyun_ekrani.blit(text0fscreen, (borderofgame + 560 , borderofgame + 40)) #hayaletsayısını oynatıyor bordera göre -ilk kısım:x ikinci:y

        oyun_ekrani.blit(spr_ghosticon, (63 - borderofgame, borderofgame - 6)) #Ghost_İcon

        text0fscreen = pygame.font.SysFont("Marker Felt", 45).render("GHOSTFIELD", True, (11, 0, 112,1)) #GhostField_label
        oyun_ekrani.blit(text0fscreen, (borderofgame + 80, borderofgame + 10))

        oyun_ekrani.blit(spr_timeicon, (borderofgame + 318, borderofgame + 10))

        text0fscreen = pygame.font.SysFont("Marker Felt", 23).render("TIME PASSED", True,(255, 131, 0, 1))  #TİME_LABEL
        oyun_ekrani.blit(text0fscreen, (borderofgame + 350, borderofgame + 10))

        oyun_ekrani.blit(spr_sghosticon, (borderofgame + 493, borderofgame + 10))

        text0fscreen = pygame.font.SysFont("Marker Felt", 23).render("GHOST COUNT", True,(255, 131, 0, 1))  # GhostCOUNT_label
        oyun_ekrani.blit(text0fscreen, (borderofgame + 525, borderofgame + 10))


        text0fscreen = pygame.font.SysFont("Marker Felt", 20).render("GAMER: ", True,(11, 0, 112,1))  # GAMER LABEL
        oyun_ekrani.blit(text0fscreen, (borderofgame + 85, borderofgame + 80))

        text0fscreen = pygame.font.SysFont("Marker Felt", 20).render(user, True,(227, 43, 94,1))  # name_label
        oyun_ekrani.blit(text0fscreen, (borderofgame + 160, borderofgame + 80))




        pygame.display.update()
        timer.tick(15)


maingame()
pygame.quit()
quit()
