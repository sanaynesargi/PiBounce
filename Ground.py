import pygame


class Ground:

    def __init__(self, window, s_width, s_height, height, color):
        self.s_width = s_width
        self.s_height = s_height

        self.width = s_width
        self.height = height

        self.x = 0
        self.y = s_height - height

        self.surface = window
        self.color = color

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height), 5)