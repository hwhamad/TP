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
    def __init__(self,levelImages,charImage,startX,startY,time,notTutorial=True):
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
        #Get the timer for each level
        self.time = time
        self.notTutorial = notTutorial
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
                    print("stop")
                    self.hSpeed = 0
                    self.vSpeed = 0
                    stop = True
                if (self.screen.get_at((newx,newy))[:3] == (34,177,76)):
                    print("cheese")
                    res = LevelResult.Result(True,self.maze.width,self.maze.height)
                    res.openResult()
    #Don't Let the Character Touch Walls to Their Right
    def avoidRightWalls(self):
        newx = self.xco + self.hSpeed + self.charWidth
        newY = range(self.yco, self.yco + self.charHeight)
        stop = False
        for newy in newY:
            if (stop == False):
                if (self.screen.get_at((newx,newy))[:3] == (0,0,0)): #or (newx,newy) in self.maze.wallsList):
                    print("stop")
                    self.hSpeed = 0
                    self.vSpeed = 0
                    stop = True
                if (self.screen.get_at((newx,newy))[:3] == (34,177,76)):
                    print("cheese")
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
                    print("stop")
                    self.hSpeed = 0
                    self.vSpeed = 0
                    stop = True
                if (self.screen.get_at((newx,newy))[:3] == (34,177,76)):
                    print("cheese")
                    res = LevelResult.Result(True,self.maze.width,self.maze.height)
                    res.openResult()
    #Don't Let the Character Touch Walls Below Them
    def avoidDownWalls(self):
        newy = self.yco + self.vSpeed + self.charHeight
        newX = range(self.xco, self.xco + self.charWidth)
        stop = False
        for newx in newX:
            if (stop == False):
                if (self.screen.get_at((newx,newy))[:3] == (0,0,0)): #or (newx,newy) in self.maze.wallsList):
                    print("stop")
                    self.hSpeed = 0
                    self.vSpeed = 0
                    stop = True
                if (self.screen.get_at((newx,newy))[:3] == (34,177,76)):
                    print("cheese")
                    res = LevelResult.Result(True,self.maze.width,self.maze.height)
                    res.openResult()
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
        #Set Up the Timer if This Isn't the Tutorial
        if (self.notTutorial):
            self.timer = Sprites.Timer(self.time)
            self.timer.txtRect.x = 30
            self.timer.txtRect.y = 30
            pygame.time.set_timer(pygame.USEREVENT, 1000)
        #Start MainLoop
        while (self.running):
            self.hSpeed = 0
            self.vSpeed = 0
            for ev in pygame.event.get():
                #Allow the User to Quit the Game
                if (ev.type == pygame.QUIT):
                    self.running = False
                    pygame.quit()
                #Update the Timer After Every Second
                if (ev.type == pygame.USEREVENT):
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
                self.hSpeed = -2
                self.avoidLeftWalls()
            if (keys[ord("d")]):
                self.hSpeed = 2
                self.avoidRightWalls()
            if (keys[ord("w")]):
                self.vSpeed = -2
                self.avoidUpWalls()
            if (keys[ord("s")]):
                self.vSpeed = 2
                self.avoidDownWalls()
            #Exit the Program, if it's No Longer Running
            if (self.running):
                #Adjust the View Depending on the View State
                if (self.viewState == 0):
                    self.screen.blit(pygame.image.load(self.image), (0,0))
                else:
                    self.screen.blit(pygame.image.load(self.image2), (0,0))
            else:
                sys.exit()
            #Change Position of Sprite
            self.xco += self.hSpeed
            self.yco += self.vSpeed
            self.char.moveX(self.hSpeed)
            self.char.moveY(self.vSpeed)
            self.allSprites.update()
            self.allSprites.draw(self.screen)
            #Update the Timer if This isn't a Tutorial
            if (self.notTutorial):
                self.screen.blit(self.timer.timer,(0,0))
            #Update the display
            pygame.display.update()
            

#137 Lines of Code When Not Considering Comments or Print Statements

#doop = openLevel(["level0.png","level0_1.png"],"charImage.png",120,400,0,False)
#doop1 = openLevel(["level1.png","level1_1.png"],"charImage.png",75,400,30)
doop2 = openLevel(["level2.png","level2_1.png"],"charImage.png",30,190,30)
doop2.createWindow()