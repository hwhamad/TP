import pygame

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
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pass

#27 Lines of Code When Not Considering Comments