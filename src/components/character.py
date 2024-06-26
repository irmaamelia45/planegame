from typing import Any
import pygame

from game import Game
from src.components.movable import Movable

class Character(pygame.sprite.Sprite, Movable):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (60,50))
        self.rect = self.image.get_rect()
        self.speed = 8
        self.player = Game.player
        Movable.__init__(self, 0, 0, 8, self.rect)
        
    def update(self):
        self.distance = self.distance + 1