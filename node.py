import functions

class Node:
    def __init__(self, char, pos):
        self.char = char
        self.i = pos[0]
        self.j = pos[1]

        self.isWall = self.char == "x" or self.char == "|" or self.char == "-"
        self.isStart = self.char == "H"
        self.isGoal = self.char == "T"
        self.isTorch = self.char == "t"
        self.isEmpty = self.char == " " or self.char == "h"

        self.crMnStp = None # current smallest step count reached by pathfinder                          # chng nm!1!!!1!!!1!
        self.maxTorchLeft = None # current maximum torch left reached by pathfinder
        self.connections = []

    def __repr__(self) -> str:
        return self.char

    def addConnection(self, node):
        self.connections.append(node)

    def addOpenConnection(self, node):
        if not node.isWall:
            self.addConnection(node)

    def setTorchLeft(self, torchLeft):
        self.maxTorchLeft = functions.maxWithNone(self.maxTorchLeft, torchLeft)

    def outConnections(self) -> str:
        out = ""
        for connection in self.connections:
            out += f"{self}->{connection}|"
        if (len(self.connections) != 0):
            out += "\n"
        return out

    def outAllConnections(nodeMatrix) -> str:
        out = ""
        for nodeRow in nodeMatrix:
            for node in nodeRow:
                out += node.outConnections()
            out += "------\n"
        return out
