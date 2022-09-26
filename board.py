import pygame


def posToString(pos):
    string = str(pos[0]) + "," + str(pos[1])
    return string


def stringToPos(string):
    array = string.split(",")
    pos = (int(array[0]), int(array[1]))
    return pos


def baseRound(x, base):
    n = x // base
    n = n * base
    return n


class Cell:
    def __init__(self, pos):
        self.pos = pos
        self.alive = False

    def kill(self):
        self.alive = False

    def revive(self):
        self.alive = True


class Board:
    def __init__(self):
        self.dimension = 2
        self.cells = {}
        self.aliveCells = []
        for y in range(-self.dimension, 800+self.dimension, self.dimension):
            for x in range(self.dimension, 1600+self.dimension, self.dimension):
                pos = str(x)+","+str(y)
                self.cells[pos] = Cell((x, y))

    def draw(self, window):
        self.get_alive()
        for cell in self.aliveCells:
            pygame.draw.rect(window, (255, 255, 255), (cell.pos[0], cell.pos[1], self.dimension, self.dimension))

    def click(self, button, pos):
        x = baseRound(pos[0], self.dimension)
        y = baseRound(pos[1], self.dimension)
        string = posToString((x, y))
        if button == 1:
            self.cells[string].revive()
        elif button == 3:
            self.cells[string].kill()

    def get_alive(self):
        self.aliveCells = []
        for cell in self.cells.values():
            if cell.alive:
                self.aliveCells.append(cell)

    def iterate(self):
        testCells = {}
        # "coords":True/False
        updateCells = {}
        for cell in self.aliveCells:
            for y in range(cell.pos[1]-self.dimension, cell.pos[1]+(2*self.dimension), self.dimension):
                for x in range(cell.pos[0]-self.dimension, cell.pos[0]+(2*self.dimension), self.dimension):
                    if 0 <= x <= 1600 and 0 <= y <= 800:
                        string = posToString((x, y))
                        testCells[string] = 0

        for key in testCells.keys():
            pos = stringToPos(key)
            for y in range(pos[1]-self.dimension, pos[1]+(2*self.dimension), self.dimension):
                for x in range(pos[0]-self.dimension, pos[0]+(2*self.dimension), self.dimension):
                    string = posToString((x, y))
                    if 0 <= x <= 1600 and 0 <= y <= 800:
                        if self.cells[string].alive:
                            testCells[key] += 1

            if self.cells[key].alive:
                testCells[key] -= 1
                if testCells[key] < 2 or testCells[key] > 3:
                    updateCells[key] = False
            else:
                if testCells[key] == 3:
                    updateCells[key] = True

        for key in updateCells.keys():
            if updateCells[key]:
                self.cells[key].revive()
            else:
                self.cells[key].kill()

    # def changeDimension(self, window, direction):
    #     if direction == "UP":
    #         self.dimension += 5
    #     elif direction == "DOWN":
    #         self.dimension -= 5
    #
    #     for item in self.cells.items():
    #         pos = item[1].pos
    #
    #         x = baseRound(pos[0], self.dimension)
    #         y = baseRound(pos[1], self.dimension)
    #
    #         item[1].pos = (baseRound(x, self.dimension), baseRound(y, self.dimension))
    #
    #         del self.cells[item[0]]
    #
    #         string = posToString((x, y))
    #         self.cells[string] = item[1]
    #
    #     self.draw(window)
