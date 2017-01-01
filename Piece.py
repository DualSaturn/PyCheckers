class piece(object):
    #class for each piece on the board
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.color = self.startColor()
        
    def startColor(self):
        green = (0, 255, 0)
        blue = (0, 0, 255)
        black = (0, 0, 0)
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
