import ImageWriter

class processMaze:
    def __init__(self,imageName):
        self.image = ImageWriter.loadPicture(imageName)
        self.height = ImageWriter.getHeight(self.image)
        self.width = ImageWriter.getWidth(self.image)

#6 Lines of Code