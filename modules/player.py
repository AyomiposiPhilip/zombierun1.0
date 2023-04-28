import math,pygame

class Player:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.jump = False
    
    def movePlayerx(self, increment):
        self.x += increment
    
    def movePlayery(self, increment):
        self.y += increment
    
    def setPlayerx(self, newx):
        self.x = newx
    
    def setPlayery(self, newy):
        self.y = newy
    
    def setCoordinates(self, newx, newy):
        self.x = newx
        self.y = newy
    
    def calculateDistanceX(self, mousex):
        xdistance = 0
        if (self.x + (self.width / 2)) > mousex:
            xdistance = (self.x + (self.width / 2)) - mousex
        elif mousex > (self.x + (self.width / 2)):
            xdistance = mousex - (self.x + (self.width / 2))
        else:
            xdistance = mousex - (self.x + (self.width / 2))
        return xdistance

    def calculateDistanceY(self, mousey):
        ydistance = 0
        if (self.y + (self.height / 2)) > mousey:
            ydistance = (self.y + (self.height / 2)) - mousey
        elif mousey > (self.y + (self.height / 2)):
            ydistance = mousey - (self.y + (self.height / 2))
        else:
            ydistance = mousey - (self.y + (self.height / 2))
        return ydistance
    
    def movement(self, keypressed):
        if keypressed[pygame.K_UP] and self.y > 0:
            self.jump = True
        
        if keypressed[pygame.K_UP] and self.y > 0:
            self.jump = True
        
        if keypressed[pygame.K_w] and self.y > 0:
            self.jump = True