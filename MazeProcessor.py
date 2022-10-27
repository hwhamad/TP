import ImageWriter

class processMaze:
    def __init__(self,imageName):
        self.image = ImageWriter.loadPicture(imageName)
        self.height = ImageWriter.getHeight(self.image)
        self.width = ImageWriter.getWidth(self.image)
class coinSave:
    def __init__(self):
        self.coins = 0

#6 Lines of Code