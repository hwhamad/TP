#Import All Necessary Libraries
import sys
import pygame
from pygame.locals import *

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
        #Start MainLoop
        while (self.running):
            #Display the Text
            self.screen.blit(text,textRect)
            #Allow the User to Quit the Program
            for ev in pygame.event.get():
                if (ev.type == pygame.QUIT):
                    self.running = False
                    pygame.quit()
            pygame.init()
            if (not self.running):
                sys.exit()
            #Update the Display
            pygame.display.update()

#35 Lines of Code When Not Considering Comments