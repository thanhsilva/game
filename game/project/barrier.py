import pygame
import random

from define import *


class Barrier():
 

    def __init__(self )-> None:
        self.set_position()

    def show(self , surface):
        self.image = pygame.image.load(img_barrier)
        self.rect = surface.blit(self.image, (self.x , self.y))

    def move(self):
        self.x -= FOOD_VELOCITY
        if(self.x < 0):
            self.set_position()

    def set_position(self):
        self.x = random.randrange(750 , WINDOW_WIDTH , BARRIER_WIDTH)
        self.y = 400

    def pause(self):
        self.x = WINDOW_WIDTH