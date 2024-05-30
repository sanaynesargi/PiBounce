import pygame


class Wall:

    def __init__(self, window, s_width, s_height, width, ground_height, color):
        self.s_width = s_width
        self.s_height = s_height
        self.ground_height = ground_height

        self.width = width
        self.height = s_height - ground_height

        self.x = 0
        self.y = 0

        self.surface = window
        self.color = color

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height), 5)