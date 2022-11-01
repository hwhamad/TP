import sys
import pygame
from pygame import *
import LevelOpening
pygame.init()

#Make a Class for Buttons
class Button:
    def __init__(self,text,topL,botR,function):
        self.text = text
        self.topL = topL
        self.botR = botR
        self.width = botR[0]-topL[0]
        self.height = botR[1] - topL[1]
        self.clickFun = function
        self.font = pygame.font.SysFont("Arial",20)

        self.activeClr = (0,255,0)
        self.deactiveClr = (0,200,0)

        self.txtSurf = self.font.render(self.text,True,(20,20,20))
        if (self.text == "Endless"):
            self.txtSurf2 = self.font.render("Mode",True,(20,20,20))
        elif (self.text == "How To"):
            self.txtSurf2 = self.font.render("Play",True,(20,20,20))
    def displayBtn(self,screen,coords,mouseXY):
        if (self.topL[0] <= mouseXY[0] and self.botR[0] >= mouseXY[0]):
            if (self.topL[1] <= mouseXY[1] and self.botR[1] >= mouseXY[1]):
                pygame.draw.rect(screen,self.activeClr,coords)
            else:
                pygame.draw.rect(screen,self.deactiveClr,coords)
        else:
            pygame.draw.rect(screen,self.deactiveClr,coords)
        if (self.text == "How To"):
            screen.blit(self.txtSurf,(coords[0]+20,coords[1]+25))
            screen.blit(self.txtSurf2,(coords[0]+32,coords[1]+45))
        elif (self.text == "Return To"):
            screen.blit(self.txtSurf,(coords[0]+20,coords[1]+25))
            screen.blit(self.txtSurf,(coords[0]+32,coords[1]+45))
        else:
            screen.blit(self.txtSurf,(coords[0]+24,coords[1]+35))


class GameOpen: #35th Line
    def __init__(self):
        self.screen = pygame.display.set_mode((500,500))
        self.titlerunning = True
        self.menurunning = True
    def openTitle(self):
        self.screen.blit(pygame.image.load("titleScreen.png"),(0,0))
        stBtn = Button("Start",(200,435),(300,485),self.mainWindow)
        while (self.titlerunning):
            mouseXY = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if (ev.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
                if (ev.type == pygame.MOUSEBUTTONDOWN):
                    if (stBtn.topL[0] <= mouseXY[0] and stBtn.botR[0] >= mouseXY[0]):
                        if (stBtn.topL[1] <= mouseXY[1] and stBtn.botR[1] >= mouseXY[1]):
                            stBtn.clickFun()
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
    def mainWindow(self):
        self.titlerunning = False
        self.screen.blit(pygame.image.load("screenBG.png"),(0,0))
        lvlBtn = Button("Levels",(125,200),(225,300),self.levelsWindow)
        endBtn = Button("Endless",(275,200),(375,300),self.endsWindow)
        while (self.menurunning):
            mouseXY = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if (ev.type == pygame.QUIT):
                    pygame.quit()
                    sys.exit()
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
    def levelsWindow(self): #101st Line
        self.menurunning = False
        self.levelsrunning = True
        self.screen.blit(pygame.image.load("screenBG.png"),(0,0))
        lvl0Btn = Button("How To",(50,100),(150,200),self.openTutorial)
        lvl1Btn = Button("Level 1",(200,100),(300,200),self.openLvl1)
        lvl2Btn = Button("Level 2",(350,100),(450,200),self.openLvl2)
        lvl3Btn = Button("Level 3",(50,300),(150,400),self.openLvl3)
        lvl4Btn = Button("Level 4",(200,300),(300,400),self.openLvl4)
        lvl5Btn = Button("Level 5",(350,300),(450,400),self.openLvl5)
        while (self.levelsrunning): 
            mouseXY = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if (ev.type == pygame.QUIT): #114
                    pygame.quit()
                    sys.exit()
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
                            lvl5Btn.clickFun() #135th Line
                    
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
    def endsWindow(self): #149th Line
        pygame.quit()
        level = LevelOpening.openLevel(["levelEndless.png","levelEndless_1.png"],"charImageSmall.png",8,480,60,False)
        level.createWindow()
    def openTutorial(self):
        pygame.quit()
        level0 = LevelOpening.openLevel(["level0.png","level0_1.png"],"charImage.png",120,400,0,False)
        level0.createWindow()
    def openLvl1(self):
        pygame.quit()
        level1 = LevelOpening.openLevel(["level1.png","level1_1.png"],"charImage.png",75,400,30)
        level1.createWindow()
    def openLvl2(self):
        pygame.quit()
        level2 = LevelOpening.openLevel(["level2.png","level2_1.png"],"charImage.png",30,190,30)
        level2.createWindow()
    def openLvl3(self):
        pygame.quit()
        level3 = LevelOpening.openLevel(["level3.png","level3_1.png"],"charImageMed.png",10,210,30)
        level3.createWindow()
    def openLvl4(self): 
        pygame.quit()
        level4 = LevelOpening.openLevel(["level4.png","level4_1.png"],"charImageSmall.png",43,40,50)
        level4.createWindow()
    def openLvl5(self):
        pygame.quit()
        level5 = LevelOpening.openLevel(["level5.png","level5_1.png"],"charImageSmall.png",9,253,65)
        level5.createWindow()
    
game = GameOpen()
game.openTitle()

#178 Lines of Code When Not Considering Comments or WhiteSpace


#540 Lines in Total