import math
import json

chessBoard = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29, 30, 31],
    [32, 33, 34, 35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44, 45, 46, 47],
    [48, 49, 50, 51, 52, 53, 54, 55],
    [56, 57, 58, 59, 60, 61, 62, 63]
]

knightMovesList = [[-1, -2], [-2, -1], [-1, 2], [-2, 1], [2, 1], [1, 2],
                   [1, -2], [2, -1]]


def solution(src, dest):
    if src == dest:
        return 0
    position = [int(math.floor(src / 8)), src % 8]
    destination = [int(math.floor(dest / 8)), dest % 8]
    visitedNodes = {}

    neighborNodes = []

    counter = 0
    while(True):
        for move in knightMovesList:
            newPosition = moveKnight(position, move)
            if isValidPosition(newPosition[0], newPosition[1]) and str(newPosition) not in visitedNodes:
                hVal = calculateDistanceFromDest(newPosition, destination)
                neighborNodes.append(Cell(newPosition, hVal, position))

        idealCell = neighborNodes[0]
        lowestHVal = float("inf")
        isFavorable = False
        for cell in neighborNodes:
            if isDestination(cell.row, cell.column, destination):
                return counter + 1
            if isFavorableCell(cell, destination):
                if isFavorable:
                    if cell.hVal < lowestHVal:
                        idealCell = cell
                        lowestHVal = cell.hVal
                else:
                    idealCell = cell
                    lowestHVal = cell.hVal
                    isFavorable = True

        if isFavorable == False:
            lowestHVal = float("inf")
            for cell in neighborNodes:
                if cell.hVal < lowestHVal:
                    idealCell = cell
                    lowestHVal = cell.hVal

        print("cell: ", idealCell)
        print(isFavorable)

        visitedNodes[str(position)] = True
        position = [idealCell.row, idealCell.column]

        neighborNodes = []
        counter += 1

    return counter + 1


def moveKnight(position, move):
    return [position[0] + move[0], position[1] + move[1]]


def isValidPosition(row, column):
    if row >= 0 and row <= 7 and column >= 0 and column <= 7:
        return True
    return False


def isDestination(row, column, dest):
    if row == dest[0] and column == dest[1]:
        return True
    return False


def calculateDistanceFromDest(node, dest):
    return abs(node[0] - dest[0]) + abs(node[1] - dest[1])


def isUnfavoraleCell(cell, dest):
    if cell.row == dest[0] or cell.column == dest[1]:
        return True
    return False


def isFavorableCell(cell, dest):
    rowDistance = abs(cell.row - dest[0])
    columnDistance = abs(cell.column - dest[1])
    if rowDistance == 0 or columnDistance == 0:
        return False
    if max(rowDistance, columnDistance) / min(rowDistance, columnDistance) == 2:
        return True
    return False


class Cell:
    def __init__(self, node, hVal, parent):
        self.row = node[0]
        self.column = node[1]
        self.hVal = hVal
        self.parent = parent

    def __repr__(self):
        return "<Cell row:%s column:%s hVal:%s parent:%s>" % (self.row, self.column, self.hVal, self.parent)


print(solution(0, 0))

# print("\n---------------------------\n")

# mem = {}

# for i in knightMovesDict.keys():
#     mem[str(knightMovesDict[i][0]) + ", " + str(knightMovesDict[i][1])] = True

# print(mem)
knightMovesDict = {
    "upOneLeft": [-1, -2],
    "upTwoLeft": [-2, -1],
    "upOneRight": [-1, 2],
    "upTwoRight": [-2, 1],
    "rightOneDown": [2, 1],
    "rightTwoDown": [1, 2],
    "rightOneUp": [-2, 1],
    "rightTwoUp": [-1, 2],
    "downOneLeft": [1, -2],
    "downTwoLeft": [2, -1],
    "downOneRight": [1, 2],
    "downTwoRight": [2, 1],
    "leftOneDown": [2, -1],
    "leftTwoDown": [1, -2],
    "leftOneUp": [-2, -1],
    "leftTwoUp": [-1, -2]


}
