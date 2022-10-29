import ImageWriter

class processMaze:
    def __init__(self,imageName):
        self.image = ImageWriter.loadPicture(imageName)
        self.height = ImageWriter.getHeight(self.image)
        self.width = ImageWriter.getWidth(self.image)
class Data:
    def __init__(self):
        fileSave = open("coinSave.txt","r")
        data = fileSave.read().split(";")
        self.curCoins = int(data[0][6:])
        self.lvl1 = False
        self.lvl2 = False
        self.lvl3 = False
        self.lvl4 = False
        self.lvl5 = False
    def save(self,coins):
        newcoins = self.curCoins + coins
        newFileSave = open("coinSave.txt","w")
        newFileSave.write(f"coins:{newcoins};")
        newFileSave.write(f"level1:{str(self.lvl1)};")
        newFileSave.write(f"level2:{str(self.lvl2)};")
        newFileSave.write(f"level3:{str(self.lvl3)};")
        newFileSave.write(f"level4:{str(self.lvl4)};")
        newFileSave.write(f"level5:{str(self.lvl5)};")
    def newGame(self):
        pass



#27 Lines of Code