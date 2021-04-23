import math


def solution(src, dest):
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

    knightMovesList = [[-1, -2], [-2, -1], [-1, 2],
                       [-2, 1], [2, 1], [1, 2], [1, -2], [2, -1]]
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

        visitedNodes[str(position)] = True
        position = [idealCell.row, idealCell.column]

        neighborNodes = []
        counter += 1

    return counter + 1


print(solution(19, 37))
