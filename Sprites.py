import pygame
import random

#Create A Sprite That's For the Character
class Char(pygame.sprite.Sprite):
    #Set the Image and Initiate the Sprite
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
    #Allow the Sprite to Move on a 2D Plane
    def moveX(self,hSpeed):
        self.rect.x += hSpeed
    def moveY(self,vSpeed):
        self.rect.y += vSpeed
#Create A Sprite That's For a Timer
class Timer(pygame.sprite.Sprite):
    #Set the Timer's Text and Initiate the Sprite
    def __init__(self,startTime):
        super().__init__()
        self.txt = str(startTime)
        self.time = startTime
        #Set the Timer's Text
        self.font = pygame.font.Font("freesansbold.ttf",32)
        self.timer = self.font.render(self.txt, True, (0,0,255),(100,100,100))
        self.txtRect = self.timer.get_rect()
    #Allow the Timer to Go Down After Every Second
    def countDown(self):
        if (self.time != 0):
            self.time -= 1
            self.txt = str(self.time)
            self.timer = self.font.render(self.txt, True, (0,0,255),(100,100,100))
            self.txtRect = self.timer.get_rect()
#Make a Sprite for the Enemy that chases the character
class Enemy(pygame.sprite.Sprite):
    #Set the Image and Initiate the Sprite
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
    #Move the Enemy closer to Player
    def moveEnemy(self,enemyCoords,playerCoords):
        self.xdir = 0
        self.ydir = 0
        if (enemyCoords[0] < playerCoords[0]):
            self.xdir = 1
        elif (enemyCoords[0] > playerCoords[0]):
            self.xdir = -1
        if (enemyCoords[1] < playerCoords[1]):
            self.ydir = 1
        elif (enemyCoords[1] > playerCoords[1]):
            self.ydir = -1
        self.rect.x += self.xdir
        self.rect.y += self.ydir
    #Check if the Enemy has reached Player
    def checkPlayer(self,enemyCoords,playerCoords,playerWH):
        #Get the Player's Dimensions
        topL = playerCoords
        topR = (topL[0] + playerWH[0], topL[1])
        botL = (topL[0], topL[1] + playerWH[1])
        botR = (topR[0], botL[1])
        #Get Enemy's Dimensions
        enemyRCoords =  (enemyCoords[0]+ self.rect.width,enemyCoords[1] + self.rect.height)
        enemyX = range(enemyCoords[0],enemyRCoords[0])
        enemyY = range(enemyCoords[1],enemyRCoords[1])
        #Check Left Side of Enemy
        for plyrLy in range(topR[1],botR[1]):
            if (enemyCoords[0] == topR[0] or enemyCoords[0] == topR[0]-1):
                if (plyrLy in enemyY):
                    return True
        #Check Bottom Side of Enemy
        for plyrBx in range(botL[0],botR[0]):
            if (enemyRCoords[1] == topL[1] or enemyRCoords[1] == topL[1]+1):
                if (plyrBx in enemyX):
                    return True
        #Check Right Side of Enemy
        for plyrRy in range(topL[1],botL[1]):
            if (enemyRCoords[0] == topL[0] or enemyRCoords[0] == topL[0]+1):
                if (plyrRy in enemyY):
                    return True
        #Check Top Side of Enemy
        for plyrUx in range(topL[0],topR[0]):
            if (enemyCoords[1] == botL[1] or enemyCoords[1] == botL[1]-1):
                if (plyrUx in enemyX):
                    return True
        return False
        #Return True if Yes
        #Return False if No

#Make a Sprite for the coins in the Endless Mode
class Coin(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
    def checkPlayer(self,coinCoords,playerCoords,playerWH):
        #Get the Player's Dimensions
        topL = playerCoords
        topR = (topL[0] + playerWH[0], topL[1])
        botL = (topL[0], topL[1] + playerWH[1])
        botR = (topR[0], botL[1])
        #Get Dimensions of Coin
        coinRCoords = (coinCoords[0]+self.rect.width,coinCoords[1]+self.rect.height)
        coinX = range(coinCoords[0],coinRCoords[0])
        coinY = range(coinCoords[1],coinRCoords[1])
        #Check Left Side of Coin
        if (topR[0] + 1 == coinCoords[0] or topR[0] == coinCoords[0]):
            for plyrRy in range(topR[1],botR[1]):
                if (plyrRy in coinY):
                    return True
        #Check Top Side of Coin
        if (botR[1] + 1 == coinCoords[1] or botR[1] == coinCoords[1]):
            for plyrBx in range(botL[0],botR[0]):
                if (plyrBx in coinX):
                    return True
        #Check Right Side of Coin
        if (botL[0] - 1 == coinRCoords[0] or botL[0] == coinRCoords[0]):
            for plyrLy in range(topL[1],botL[1]):
                if (plyrLy in coinY):
                    return True
        #Check Bottom Side of Coin
        if (topL[1] - 1 == coinRCoords[1] or topL[1] == coinRCoords[1]):
            for plyrTx in range(topL[0],topR[0]):
                if (plyrTx in coinX):
                    return True
        return False
    def changeLocation(self,coinCoords): #99th Line
        allCoords = [(535,90), (65,285), (201,422), (90,145), (506,477), (229,7), (478,340)]
        newCoords = coinCoords
        while (coinCoords == newCoords):
            newCoords = random.choice(allCoords)
        self.rect.x = newCoords[0]
        self.rect.y = newCoords[1]


#105 Lines of Code When Not Considering Comments