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

    def update(self, move_x, move_y):
        last_x = self.x
        last_y = self.y

        self.x += move_x
        self.y += move_y

        if self.x < 0 or self.x + GameConfig.BODY_SIZE > GameConfig.SCREEN_WEIGHT:
            self.gameOver = True

        if self.y < 0 or self.y + GameConfig.BODY_SIZE > GameConfig.SCREEN_HEIGHT:
            self.gameOver = True

        for element in self.elements:
            x = element.x
            y = element.y
            element.x = last_x
            element.y = last_y
            last_x = x
            last_y = y

    def isGameOver(self):
        return self.gameOver == True


class Element():
    def __init__(self, x, y):
        self.x = x
        self.y = y
