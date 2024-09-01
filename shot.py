import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        self.SHOT_RADIUS = 5
        super().__init__(x, y, SHOT_RADIUS)

