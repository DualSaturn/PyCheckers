import pygame
import math

green = (0, 255, 0)
blue = (0, 100, 255)
black = (0, 0, 0)
white = (255, 255, 255)

class piece(object):
    #class for each piece on the board
    def __init__(self, row, column, x, y, surf):
        self.row = row
        self.column = column
        self.color = self.startColor()
        self.pos_x = int(x)
        self.pos_y = int(y)
        self.surf = surf

    def startColor(self):
        col = black
        if self.row % 2 == 0:
            if self.row <= 2:
                if self.column % 2 == 1:
                    col = green
                else:
                    col = black
            elif self.row >= 5:
                if self.column % 2 == 1:
                    col = blue
                else:
                    col = black
        else:
            if self.row <= 2:
                if self.column % 2 == 0:
                    col = green
                else:
                    col = black
            elif self.row >= 5:
                if self.column % 2 == 0:
                    col = blue
                else:
                    col = black

        return col

    def draw(self):
        pygame.draw.circle(self.surf, self.color, (self.pos_x, self.pos_y), 20)

    def clicked(self, click_x, click_y):
        dist = math.hypot(click_x - self.pos_x, click_y - self.pos_y)
        if dist>20:
            return False
        else:
            return True

    def handleClick(self, click_x, click_y):
        if self.clicked(click_x, click_y):
            if self.color != black:
                self.color = white
