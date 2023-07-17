# -*- coding: utf-8 -*-

import pygame

from src.state import GameState
from src.config import GameConfig
from src import unit


class Game():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((
            GameConfig.SCREEN_WEIGHT,
            GameConfig.SCREEN_HEIGHT
        ))
        pygame.display.set_caption("Snake for Zoe")
        pygame.display.set_icon(pygame.image.load("img/icon.png"))
        self.clock = pygame.time.Clock()
        self.gameState = GameState()
        self.snake = unit.Snake(self.gameState)
        # pygame.key.set_repeat(1, 100)
        self.moveCommandX = 0
        self.moveCommandY = 0
        self.running = True

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                self.moveCommandX = 0
                self.moveCommandY = 0
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    self.running = False
                    break
                if keys[pygame.K_RIGHT]:
                    self.moveCommandX = GameConfig.STEP
                if keys[pygame.K_LEFT]:
                    self.moveCommandX = -GameConfig.STEP
                if keys[pygame.K_DOWN]:
                    self.moveCommandY = GameConfig.STEP
                if keys[pygame.K_UP]:
                    self.moveCommandY = -GameConfig.STEP

    def update(self):
        self.gameState.update(self.moveCommandX, self.moveCommandY)

    def render(self):
        unit.Background.render()

        if self.gameState.isGameOver():
            unit.GameOver.render()
        else:
            self.snake.render()

        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(GameConfig.SCREEN_FRAMES_PER_SECOND)
