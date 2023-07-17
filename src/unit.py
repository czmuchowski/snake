# -*- coding: utf-8 -*-
import pygame
from pygame import Rect
from src.config import GameConfig


class Background:
    @staticmethod
    def render():
        screen = pygame.display.get_surface()
        color = (0, 0, 0)
        screen.fill(color)


class GameOver:
    @staticmethod
    def render():
        pygame.font.init()
        screen = pygame.display.get_surface()
        color = (255, 0, 0)
        font = pygame.font.SysFont('Comic Sans MS', 40)
        text = font.render("Game Over", True, color)
        screen.blit(text, (400, 300))


class Snake():
    def __init__(self, game_state):
        self.screen = pygame.display.get_surface()
        self.gameState = game_state
        self.texture_head = pygame.image.load("img/snake_head_48x48.png").convert_alpha()
        self.texture_body = pygame.image.load("img/snake_body_48x48.png").convert_alpha()

    def render_head(self, x, y):
        texture_rect = Rect(0, 0, GameConfig.BODY_SIZE, GameConfig.BODY_SIZE)
        self.screen.blit(self.texture_head, (x, y), texture_rect)

    def render_body(self, x, y):
        texture_rect = Rect(0, 0, GameConfig.BODY_SIZE, GameConfig.BODY_SIZE)
        self.screen.blit(self.texture_body, (x, y), texture_rect)

    def render(self):
        for element in self.gameState.elements:
            self.render_body(element.x, element.y)
        self.render_head(self.gameState.x, self.gameState.y)
