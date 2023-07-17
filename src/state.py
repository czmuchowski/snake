# -*- coding: utf-8 -*-

from src.config import GameConfig

class GameState():
    def __init__(self):
        self.gameOver = False
        self.x = 300
        self.y = 200
        self.elements = [
            Element(self.x - GameConfig.BODY_SIZE, self.y),
            Element(self.x - GameConfig.BODY_SIZE, self.y),
            Element(self.x - GameConfig.BODY_SIZE, self.y)
        ]
        

    def update(self ,moveX, moveY):
        lastX = self.x
        lastY = self.y
        
        self.x += moveX
        self.y += moveY
        
        if self.x < 0 or self.x + GameConfig.BODY_SIZE > GameConfig.SCREEN_WEIGHT:
            self.gameOver = True

        if self.y < 0 or self.y + GameConfig.BODY_SIZE > GameConfig.SCREEN_HEIGHT:
            self.gameOver = True
            
        for element in self.elements:
            x = element.x
            y = element.y
            element.x = lastX
            element.y = lastY
            lastX = x
            lastY = y
            
    
    def isGameOver(self):
        return self.gameOver == True
    
    def addElement(self):
        self.elements.append(Element())
        
        
class Element():
    def __init__(self, x, y):
        self.x = x
        self.y = y
