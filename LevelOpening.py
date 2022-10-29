#Import All Additional Files and Libraries
import sys
import pygame
from pygame.locals import *
from MazeProcessor import *
import LevelResult
import Sprites

#Create A Class that'll be called whenever we want to open a level
class openLevel:
    #Initialize All Values and Images for the Class
    def __init__(self,levelImages,charImage,startX,startY,time,timerLvl=True):
        #Get all the Images and Values for a Level
        pygame.init()
        self.running = True
        self.image = levelImages[0]
        self.maze = processMaze(levelImages[0])
        self.image2 = levelImages[1]
        self.maze2 = processMaze(levelImages[1])
        self.viewState = 0
        #Set the Location and State of the Character
        self.xco = startX
        self.yco = startY
        self.hSpeed = 0
        self.vSpeed = 0
        self.charImage = charImage
        self.spd = 2
        if (self.charImage == "charImageSmall.png" or self.charImage == "charImageMed.png"):
            self.spd = 1
        #Get the timer for each level
        self.time = time
        self.timerLvl = timerLvl
        #Check if this is endless mode
        self.endLevel = False
        if (self.image == "levelEndless.png"):
            self.endLevel = True
            self.enmTime = 1000
            self.coins = 0
        #Create a Group for all Sprites
        self.allSprites = pygame.sprite.Group()
    #Don't Let the Character Touch Walls to Their Left
    def avoidLeftWalls(self):
        newx = self.xco + self.hSpeed
        newY = range(self.yco, self.yco + self.charHeight)
        stop = False
        for newy in newY:
            if (stop == False):
                if (self.screen.get_at((newx,newy))[:3] == (0,0,0)): #or (newx,newy) in self.maze.wallsList):
                    self.hSpeed = 0
                    self.vSpeed = 0
                    stop = True
                if (self.screen.get_at((newx,newy))[:3] == (34,177,76)):
                    res = LevelResult.Result(True,self.maze.width,self.maze.height)
                    res.openResult()
    #Don't Let the Character Touch Walls to Their Right
    def avoidRightWalls(self): #45th line
        newx = self.xco + self.hSpeed + self.charWidth
        newY = range(self.yco, self.yco + self.charHeight)
        stop = False
        for newy in newY:
            if (stop == False):
                if (self.screen.get_at((newx,newy))[:3] == (0,0,0)): #or (newx,newy) in self.maze.wallsList):
                    self.hSpeed = 0
                    self.vSpeed = 0
                    stop = True
                if (self.screen.get_at((newx,newy))[:3] == (34,177,76)):
                    res = LevelResult.Result(True,self.maze.width,self.maze.height)
                    res.openResult()
    #Don't Let the Character Touch Walls Above Them
    def avoidUpWalls(self):
        newy = self.yco + self.vSpeed
        newX = range(self.xco, self.xco + self.charWidth)
        stop = False
        for newx in newX:
            if (stop == False):
                if (self.screen.get_at((newx,newy))[:3] == (0,0,0)): #or (newx,newy) in self.maze.wallsList):
                    self.hSpeed = 0
                    self.vSpeed = 0
                    stop = True
                if (self.screen.get_at((newx,newy))[:3] == (34,177,76)):
                    res = LevelResult.Result(True,self.maze.width,self.maze.height)
                    res.openResult()
    #Don't Let the Character Touch Walls Below Them
    def avoidDownWalls(self):
        newy = self.yco + self.vSpeed + self.charHeight
        newX = range(self.xco, self.xco + self.charWidth)
        stop = False
        for newx in newX:
            if (stop == False):
                if (self.screen.get_at((newx,newy))[:3] == (0,0,0)): 
                    self.hSpeed = 0
                    self.vSpeed = 0
                    stop = True
                if (self.screen.get_at((newx,newy))[:3] == (34,177,76)):
                    res = LevelResult.Result(True,self.maze.width,self.maze.height)
                    res.openResult()
    #Enable the Endless Sprites
    def enableSprite(self):
        self.enemy = Sprites.Enemy("enemy.png")
        self.enemy.rect.x = 8
        self.enemy.rect.y = 10
        self.coin = Sprites.Coin("coin.png")
        self.coin.rect.x = 535
        self.coin.rect.y = 90
        self.allSprites.add(self.enemy)
        self.allSprites.add(self.coin)
    def checkEnemy(self):
        enemyco = (self.enemy.rect.x,self.enemy.rect.y)
        playerDimensions = (self.charWidth,self.charHeight)
        enemyreached = self.enemy.checkPlayer(enemyco,(self.xco,self.yco),playerDimensions)
        if (enemyreached):
            res = LevelResult.Result(False,self.maze.width,self.maze.height)
            res.openResult()
    def checkCoin(self): #100th Line
        coinco = (self.coin.rect.x,self.coin.rect.y)
        playerWH = (self.char.rect.width,self.char.rect.height)
        coinreached = self.coin.checkPlayer(coinco,(self.xco,self.yco),playerWH)
        if (coinreached):
            self.coin.changeLocation(coinco)
            self.coins += 1
            Data().save(self.coins)
            self.enmTime //= 2
            pygame.time.set_timer(pygame.USEREVENT,self.enmTime)
    #Create A New Window and Put All Sprites on the Screen
    def createWindow(self):
        #Display the Screen and Find the Character's Attributes
        self.screen = pygame.display.set_mode((self.maze.width , self.maze.height))
        self.screen.blit(pygame.image.load(self.image), (0,0))
        self.char = Sprites.Char(self.charImage)
        self.char.rect.x = self.xco
        self.char.rect.y = self.yco
        self.charWidth = self.char.rect.width
        self.charHeight = self.char.rect.height
        self.allSprites.add(self.char)
        #Create Enemy Sprite if Necessary
        if (self.endLevel):
            self.enableSprite()
        #Set Up the Timer if This Isn't the Tutorial
        if (self.timerLvl):
            self.timer = Sprites.Timer(self.time)
            self.timer.txtRect.x = 100
            self.timer.txtRect.y = 100
            pygame.time.set_timer(pygame.USEREVENT, 1000)
        #Set Up the Enemy's Movement if This is Endless Mode
        if (self.endLevel):
            pygame.time.set_timer(pygame.USEREVENT,self.enmTime)
        #Start MainLoop
        while (self.running):
            self.hSpeed = 0
            self.vSpeed = 0
            for ev in pygame.event.get():
                #Allow the User to Quit the Game
                if (ev.type == pygame.QUIT):
                    self.running = False
                    pygame.quit()
                #Update the Following out of USEREVENT
                if (ev.type == pygame.USEREVENT):
                    #Check if we're in Endless Mode
                    if (self.endLevel):
                        #Update the Enemy's Movement
                        enemyco = (self.enemy.rect.x,self.enemy.rect.y)
                        self.enemy.moveEnemy(enemyco,(self.xco,self.yco))
                        #Check if they've touched the player
                        if (self.enemy.xdir == 0 and self.enemy.ydir == 0):
                            res = LevelResult.Result(False,self.maze.width,self.maze.height)
                            res.openResult()
                        self.checkEnemy()
                    #Update the Timer if Necessary
                    if (self.timerLvl):
                        self.timer.countDown()
                        if (self.timer.time == 0):
                            res = LevelResult.Result(False,self.maze.width,self.maze.height)
                            res.openResult()
                #If someone presses a key, it causes something in the game:
                #Pressing ESC quits the game
                #Pressing SPACE shifts the view
                if (ev.type == pygame.KEYDOWN):
                    if (ev.key == pygame.K_ESCAPE):
                        pygame.quit()
                        self.running = False
                    if (ev.key == pygame.K_SPACE):
                        self.viewState = (self.viewState + 1) % 2
            #Control the character's movement with WASD
            pygame.init()
            keys = pygame.key.get_pressed()
            if (keys[ord("a")]):
                self.hSpeed = self.spd * -1
                self.avoidLeftWalls()
                #Check if They Touched the Enemy
                if (self.endLevel):
                    self.checkEnemy()
                    self.checkCoin()
            if (keys[ord("d")]):
                self.hSpeed = self.spd
                self.avoidRightWalls()
                #Check if They Touched the Enemy
                if (self.endLevel):
                    self.checkEnemy()
                    self.checkCoin()
            if (keys[ord("w")]):
                self.vSpeed = self.spd * -1
                self.avoidUpWalls()
                #Check if They Touched the Enemy
                if (self.endLevel):
                    self.checkEnemy()
                    self.checkCoin()
            if (keys[ord("s")]):
                self.vSpeed = self.spd
                self.avoidDownWalls()
                #Check if They Touched the Enemy
                if (self.endLevel):
                    self.checkEnemy()
                    self.checkCoin()
            #Exit the Program, if it's No Longer Running
            if (self.running):
                #Adjust the View Depending on the View State
                if (self.viewState == 0):
                    self.screen.blit(pygame.image.load(self.image), (0,0))
                else:
                    self.screen.blit(pygame.image.load(self.image2), (0,0))
            else:
                sys.exit()
            #Update the Timer if This isn't a Tutorial
            if (self.timerLvl):
                self.screen.blit(self.timer.timer,(1,1))    
            #Change Position of Sprite
            self.xco += self.hSpeed
            self.yco += self.vSpeed
            self.char.moveX(self.hSpeed)
            self.char.moveY(self.vSpeed)
            self.allSprites.update()
            self.allSprites.draw(self.screen)
            #Update the display
            pygame.display.update()
            

#195 Lines of Code When Not Considering Comments or Print Statements
