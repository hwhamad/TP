import sys
import pygame
from pygame import *
from MazeProcessor import *
import Sprites
pygame.init()

#Make a Class for Buttons
class Button:
    #Initialize all the button's properties
    def __init__(self,text,topL,botR,function):
        pygame.init()
        self.text = text
        self.topL = topL
        self.botR = botR
        self.width = botR[0]-topL[0]
        self.height = botR[1] - topL[1]
        self.clickFun = function
        self.font = pygame.font.SysFont("Arial",20)
        #Set the colors of the buttons
        self.activeClr = (20,255,20)
        self.deactiveClr = (20,200,20)
        #Set the text of the buttons
        self.txtSurf = self.font.render(self.text,True,(20,20,20))
        if (self.text == "Endless"):
            self.txtSurf2 = self.font.render("Mode",True,(20,20,20))
        elif (self.text == "How To"):
            self.txtSurf2 = self.font.render("Play",True,(20,20,20))
    #Create a function to display the button on the screen
    def displayBtn(self,screen,coords,mouseXY):
        #Set the button to the correct color
        if (self.topL[0] <= mouseXY[0] and self.botR[0] >= mouseXY[0]):
            if (self.topL[1] <= mouseXY[1] and self.botR[1] >= mouseXY[1]):
                pygame.draw.rect(screen,self.activeClr,coords)
            else:
                pygame.draw.rect(screen,self.deactiveClr,coords)
        else:
            pygame.draw.rect(screen,self.deactiveClr,coords)
        #Display the text on the button
        if (self.text == "How To"):
            screen.blit(self.txtSurf,(coords[0]+20,coords[1]+25))
            screen.blit(self.txtSurf2,(coords[0]+32,coords[1]+45))
        elif (self.text == "Return To"):
            screen.blit(self.txtSurf,(coords[0]+20,coords[1]+25))
            screen.blit(self.txtSurf,(coords[0]+32,coords[1]+45))
        else:
            screen.blit(self.txtSurf,(coords[0]+24,coords[1]+35))

#Make a Class For Starting the Game
class GameOpen: 
    #Initialize the window
    def __init__(self):
        self.screen = pygame.display.set_mode((500,500))
        self.titlerunning = True
        self.menurunning = True
    #Open the Title Screen
    def openTitle(self):
        self.screen.blit(pygame.image.load("titleScreen.png"),(0,0))
        stBtn = Button("Start",(200,435),(300,485),self.mainWindow)
        #Start the Main Loop
        while (self.titlerunning):
            mouseXY = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if (ev.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                #Allow the Button to Start the Game
                if (ev.type == pygame.MOUSEBUTTONDOWN):
                    if (stBtn.topL[0] <= mouseXY[0] and stBtn.botR[0] >= mouseXY[0]):
                        if (stBtn.topL[1] <= mouseXY[1] and stBtn.botR[1] >= mouseXY[1]):
                            stBtn.clickFun()
            #Display the Start Button
            coords = [stBtn.topL[0],stBtn.topL[1],stBtn.width,stBtn.height]
            if (stBtn.topL[0] <= mouseXY[0] and stBtn.botR[0] >= mouseXY[0]):
                if (stBtn.topL[1] <= mouseXY[1] and stBtn.botR[1] >= mouseXY[1]):
                    pygame.draw.rect(self.screen,stBtn.activeClr,coords)
                else:
                    pygame.draw.rect(self.screen,stBtn.deactiveClr,coords)
            else:
                pygame.draw.rect(self.screen,stBtn.deactiveClr,coords)
            self.screen.blit(stBtn.txtSurf,(coords[0]+30,coords[1]+10))
            pygame.display.update()
    #Open the Main Menu Window
    def mainWindow(self):
        self.titlerunning = False
        self.screen.blit(pygame.image.load("screenBG.png"),(0,0))
        lvlBtn = Button("Levels",(125,200),(225,300),self.levelsWindow)
        endBtn = Button("Endless",(275,200),(375,300),self.endsWindow)
        #Start the Main Loop
        while (self.menurunning):
            mouseXY = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if (ev.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                #Allow the Buttons to Work
                if (ev.type == pygame.MOUSEBUTTONDOWN):
                    #Check if they clicked the levels button
                    if (lvlBtn.topL[0] <= mouseXY[0] and lvlBtn.botR[0] >= mouseXY[0]):
                        if (lvlBtn.topL[1] <= mouseXY[1] and lvlBtn.botR[1] >= mouseXY[1]):
                            lvlBtn.clickFun()
                    #Check if they clicked the endless mode button
                    if (endBtn.topL[0] <= mouseXY[0] and endBtn.botR[0] >= mouseXY[0]):
                        if (endBtn.topL[1] <= mouseXY[1] and endBtn.botR[1] >= mouseXY[1]):
                            endBtn.clickFun()
            #Check if their mouse is over the levels button and draw it
            coords = [lvlBtn.topL[0],lvlBtn.topL[1],lvlBtn.width,lvlBtn.height]
            if (lvlBtn.topL[0] <= mouseXY[0] and lvlBtn.botR[0] >= mouseXY[0]):
                if (lvlBtn.topL[1] <= mouseXY[1] and lvlBtn.botR[1] >= mouseXY[1]):
                    pygame.draw.rect(self.screen,lvlBtn.activeClr,coords)
                else:
                    pygame.draw.rect(self.screen,lvlBtn.deactiveClr,coords)
            else:
                pygame.draw.rect(self.screen,lvlBtn.deactiveClr,coords)
            self.screen.blit(lvlBtn.txtSurf,(coords[0]+27,coords[1]+35))
            #Check if their mouse is over the endless mode button and draw it
            coordsE = [endBtn.topL[0],endBtn.topL[1],endBtn.width,endBtn.height]
            if (endBtn.topL[0] <= mouseXY[0] and endBtn.botR[0] >= mouseXY[0]):
                if (endBtn.topL[1] <= mouseXY[1] and endBtn.botR[1] >= mouseXY[1]):
                    pygame.draw.rect(self.screen,endBtn.activeClr,coordsE)
                else:
                    pygame.draw.rect(self.screen,endBtn.deactiveClr,coordsE)
            else:
                pygame.draw.rect(self.screen,endBtn.deactiveClr,coordsE)
            self.screen.blit(endBtn.txtSurf,(coordsE[0]+22,coordsE[1]+25))
            self.screen.blit(endBtn.txtSurf2,(coordsE[0]+32,coordsE[1]+45))
            pygame.display.update()
    #Open the Level Select Window
    def levelsWindow(self):
        self.menurunning = False
        self.levelsrunning = True
        self.screen.blit(pygame.image.load("screenBG.png"),(0,0))
        #Initialize all the Buttons
        lvl0Btn = Button("How To",(50,100),(150,200),self.openTutorial)
        lvl1Btn = Button("Level 1",(200,100),(300,200),self.openLvl1)
        lvl2Btn = Button("Level 2",(350,100),(450,200),self.openLvl2)
        lvl3Btn = Button("Level 3",(50,300),(150,400),self.openLvl3)
        lvl4Btn = Button("Level 4",(200,300),(300,400),self.openLvl4)
        lvl5Btn = Button("Level 5",(350,300),(450,400),self.openLvl5)
        #Start the Main Loop
        while (self.levelsrunning): 
            mouseXY = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if (ev.type == pygame.QUIT): #114
                    pygame.quit()
                    sys.exit()
                #Allow the buttons to send you to the correct
                if (ev.type == pygame.MOUSEBUTTONDOWN):
                    #Check if they clicked the tutorial button
                    if (lvl0Btn.topL[0] <= mouseXY[0] and lvl0Btn.botR[0] >= mouseXY[0]):
                        if (lvl0Btn.topL[1] <= mouseXY[1] and lvl0Btn.botR[1] >= mouseXY[1]):
                            lvl0Btn.clickFun()
                    #Check if they clicked the level 1 button
                    if (lvl1Btn.topL[0] <= mouseXY[0] and lvl1Btn.botR[0] >= mouseXY[0]):
                        if (lvl1Btn.topL[1] <= mouseXY[1] and lvl1Btn.botR[1] >= mouseXY[1]):
                            lvl1Btn.clickFun()
                    #Check if they cliked the level 2 button
                    if (lvl2Btn.topL[0] <= mouseXY[0] and lvl2Btn.botR[0] >= mouseXY[0]):
                        if (lvl2Btn.topL[1] <= mouseXY[1] and lvl2Btn.botR[1] >= mouseXY[1]):
                            lvl2Btn.clickFun()
                    #Check if they clicked the level 3 button
                    if (lvl3Btn.topL[0] <= mouseXY[0] and lvl3Btn.botR[0] >= mouseXY[0]):
                        if (lvl3Btn.topL[1] <= mouseXY[1] and lvl3Btn.botR[1] >= mouseXY[1]):
                            lvl3Btn.clickFun()
                    #Check if they clicked the level 4 button
                    if (lvl4Btn.topL[0] <= mouseXY[0] and lvl4Btn.botR[0] >= mouseXY[0]):
                        if (lvl4Btn.topL[1] <= mouseXY[1] and lvl4Btn.botR[1] >= mouseXY[1]):
                            lvl4Btn.clickFun()
                    #Check if they clicked the level 5 button
                    if (lvl5Btn.topL[0] <= mouseXY[0] and lvl5Btn.botR[0] >= mouseXY[0]):
                        if (lvl5Btn.topL[1] <= mouseXY[1] and lvl5Btn.botR[1] >= mouseXY[1]):
                            lvl5Btn.clickFun()
                    
            #Check if their mouse is over the level 0 button and draw it
            coords0 = [lvl0Btn.topL[0],lvl0Btn.topL[1],lvl0Btn.width,lvl0Btn.height]
            lvl0Btn.displayBtn(self.screen,coords0,mouseXY)

            #Check if their mouse is over the level 1 button and draw it
            coords1 = [lvl1Btn.topL[0],lvl1Btn.topL[1],lvl1Btn.width,lvl1Btn.height]
            lvl1Btn.displayBtn(self.screen,coords1,mouseXY)
            
            #Check if their mouse is over the level 2 button and draw it
            coords2 = [lvl2Btn.topL[0],lvl2Btn.topL[1],lvl2Btn.width,lvl2Btn.height]
            lvl2Btn.displayBtn(self.screen,coords2,mouseXY)

            #Check if their mouse is over the level 3 button and draw it
            coords3 = [lvl3Btn.topL[0],lvl3Btn.topL[1],lvl3Btn.width,lvl3Btn.height]
            lvl3Btn.displayBtn(self.screen,coords3,mouseXY)

            #Check if their mouse is over the level 4 button and draw it
            coords4 = [lvl4Btn.topL[0],lvl4Btn.topL[1],lvl4Btn.width,lvl4Btn.height]
            lvl4Btn.displayBtn(self.screen,coords4,mouseXY)

            #Check if their mouse is over the level 5 button and draw it
            coords5 = [lvl5Btn.topL[0],lvl5Btn.topL[1],lvl5Btn.width,lvl5Btn.height]
            lvl5Btn.displayBtn(self.screen,coords5,mouseXY)
            
            pygame.display.update()
    #Open the Endless Mode
    def endsWindow(self): #149th Line
        pygame.quit()
        level = openLevel(["levelEndless.png","levelEndless_1.png"],"charImageSmall.png",8,480,60,False)
        level.createWindow()
    #Open the Tutorial
    def openTutorial(self):
        pygame.quit()
        level0 = openLevel(["level0.png","level0_1.png"],"charImage.png",120,400,0,False)
        level0.createWindow()
    #Open Level 1
    def openLvl1(self):
        pygame.quit()
        level1 = openLevel(["level1.png","level1_1.png"],"charImage.png",75,400,30)
        level1.createWindow()
    #Open Level 2
    def openLvl2(self):
        pygame.quit()
        level2 = openLevel(["level2.png","level2_1.png"],"charImage.png",30,190,30)
        level2.createWindow()
    #Open Level 3
    def openLvl3(self):
        pygame.quit()
        level3 = openLevel(["level3.png","level3_1.png"],"charImageMed.png",10,210,30)
        level3.createWindow()
    #Open Level 4
    def openLvl4(self): 
        pygame.quit()
        level4 = openLevel(["level4.png","level4_1.png"],"charImageSmall.png",43,40,50)
        level4.createWindow()
    #Open Level 5
    def openLvl5(self):
        pygame.quit()
        level5 = openLevel(["level5.png","level5_1.png"],"charImageSmall.png",9,253,65)
        level5.createWindow()

#Make a Class for Opening a Level from Level Select
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
                    res = Result(True,self.maze.width,self.maze.height)
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
                    res = Result(True,self.maze.width,self.maze.height)
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
                    res = Result(True,self.maze.width,self.maze.height)
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
                    res = Result(True,self.maze.width,self.maze.height)
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
    #Check if the player has touched the enemy
    def checkEnemy(self):
        enemyco = (self.enemy.rect.x,self.enemy.rect.y)
        playerDimensions = (self.charWidth,self.charHeight)
        enemyreached = self.enemy.checkPlayer(enemyco,(self.xco,self.yco),playerDimensions)
        #End the Game
        if (enemyreached):
            res = Result(False,self.maze.width,self.maze.height)
            res.openResult()
    #Check if the player has touched the coin
    def checkCoin(self):
        coinco = (self.coin.rect.x,self.coin.rect.y)
        playerWH = (self.char.rect.width,self.char.rect.height)
        coinreached = self.coin.checkPlayer(coinco,(self.xco,self.yco),playerWH)
        #Save the coin and change its location
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
                            res = Result(False,self.maze.width,self.maze.height)
                            res.openResult()
                        self.checkEnemy()
                    #Update the Timer if Necessary
                    if (self.timerLvl):
                        self.timer.countDown()
                        if (self.timer.time == 0):
                            res = Result(False,self.maze.width,self.maze.height)
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

#Create A Class that Manages When A Level is Finished
class Result:
    #Initialize All Values For When A Player Wins or Loses
    def __init__(self,winStatus,width,height):
        pygame.init()
        self.win = winStatus
        #Set the Text and Colors Depending on the Result
        if (self.win):
            self.resultText = "Well Done!"
            self.txtcolor = (0,255,0)
            self.scrcolor = (255,255,255)
        else:
            self.resultText = "GAME OVER"
            self.txtcolor = (255,0,0)
            self.scrcolor = (0,0,0)
        #Set the Values of the Screen
        self.width = width
        self.height = height
        self.running = True
    #Set the Screen to Display the Corresponding Result
    def openResult(self):
        #Show the Screen with the Correct Text
        self.screen = pygame.display.set_mode((self.width , self.height))
        self.screen.fill(self.scrcolor)
        font = pygame.font.Font("freesansbold.ttf",32)
        text = font.render(self.resultText, True, self.txtcolor)
        textRect = text.get_rect()
        textRect.center = (self.width//2,self.height//2)
        rtnBtn = Button("Return",(self.width//2 -50,350),(self.width//2 +50,450),self.returnFun)
        #Start MainLoop
        while (self.running):
            #Get the mouse's position
            mouseXY = pygame.mouse.get_pos()
            #Display the Text
            self.screen.blit(text,textRect)
            #Allow the User to Quit the Program
            for ev in pygame.event.get():
                if (ev.type == pygame.QUIT):
                    self.running = False
                    pygame.quit()
                if (ev.type == pygame.MOUSEBUTTONDOWN):
                    #Check if they clicked the return button
                    if (rtnBtn.topL[0] <= mouseXY[0] and rtnBtn.botR[0] >= mouseXY[0]):
                        if (rtnBtn.topL[1] <= mouseXY[1] and rtnBtn.botR[1] >= mouseXY[1]):
                            rtnBtn.clickFun()
            #Check if their mouse is over the return button and draw it
            coords = [rtnBtn.topL[0],rtnBtn.topL[1],rtnBtn.width,rtnBtn.height]
            rtnBtn.displayBtn(self.screen,coords,mouseXY)
            pygame.init()
            if (not self.running):
                sys.exit()
            #Update the Display
            pygame.display.update()
    #Return to the Main Menu
    def returnFun(self):
        pygame.quit()
        restart = GameOpen()
        restart.mainWindow()

#Start the Program
game = GameOpen()
game.openTitle()
