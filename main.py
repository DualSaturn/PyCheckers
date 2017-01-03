#main file for checkers game
from Piece import piece
import pygame
pygame.init()

#initializing values
surfaceWidth = 750
surfaceHeight = 750
boardWidth = 500
boardHeight = 500
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
clock = pygame.time.Clock()

#creating game surface
gameSurface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption("PyCheckers")

#creating board
#board = [[piece(i, j) for j in range(8)] for i in range(8)]
board = []
def createBoard():
    xCoordinate = 156.25
    yCoordinate = 156.25
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(piece(i, j, xCoordinate, yCoordinate, gameSurface))
            xCoordinate = xCoordinate + 62.5
        yCoordinate = yCoordinate + 62.5
        xCoordinate = 156.25


def resetBoard():
    for i in range(8):
        for j in range(8):
            board[i][j].color = board[i][j].startColor()

#function to draw all pieces
def drawPieces():
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j].draw()

#function to draw the board's outline
def drawBoardOutline():
    lines = [
    ((125, 625), (625, 625)), #bottom
    ((125, 125), (625, 125)), #top
    ((625, 125), (625, 625)), #right
    ((125, 125), (125, 625)), #left
    ((125 + boardWidth/2, 125), (125 + boardWidth/2, 625)), #vertical 1/2
    ((125, 125 + boardHeight/2), (625, 125 + boardHeight/2)), #horizontal 1/2
    ((125 + boardWidth/4, 125), (125 + boardWidth/4, 625)), #vertical 1/4
    ((125, 125 + boardHeight/4), (625, 125 + boardHeight/4)), #horizontal 1/4
    ((125 + 3*boardWidth/4, 125), (125 + 3*boardWidth/4, 625)), #vertical 3/4
    ((125, 125 + 3*boardHeight/4), (625, 125 + 3*boardHeight/4)), #horizontal 3/4
    ((125 + boardWidth/8, 125), (125 + boardWidth/8, 625)), #vertical 1/8
    ((125, 125 + boardHeight/8), (625, 125 + boardHeight/8)), #horizontal 1/8
    ((125 + 3*boardWidth/8, 125), (125 + 3*boardWidth/8, 625)), #vertical 3/8
    ((125, 125 + 3*boardHeight/8), (625, 125 + 3*boardHeight/8)), #horizontal 3/8
    ((125 + 5*boardWidth/8, 125), (125 + 5*boardWidth/8, 625)), #vertical 5/8
    ((125, 125 + 5*boardHeight/8), (625, 125 + 5*boardHeight/8)), #horizontal 5/8
    ((125 + 7*boardWidth/8, 125), (125 + 7*boardWidth/8, 625)), #vertical 7/8
    ((125, 125 + 7*boardHeight/8), (625, 125 + 7*boardHeight/8)) #horizontal 7/8
    ]
    for x in lines:
        pygame.draw.line(gameSurface, white, x[0], x[1], 3)

#main game loop
createBoard()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameSurface.fill(black)
    drawBoardOutline()
    drawPieces()
    pygame.display.update()
    clock.tick(60)
