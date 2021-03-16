class Node:
    def __init__(self, char):
        self.char = char
        
        self.isWall = self.char == "x" or self.char == "|" or self.char == "-"
        self.isStart = self.char == "H"
        self.isGoal = self.char == "T"
        self.isTorch = self.char == "t"
        self.isEmpty = self.char == " "

        self.crMnStp = -1 # current smallest step count reached by pathfinder                          # chng nm!1!!!1!!!1!
        self.connections = []

    def __repr__(self) -> str:
        return self.char

    def addConnection(self, node):
        self.connections.append(node)

    def addOpenConnection(self, node):
        if not node.isWall:
            self.addConnection(node)

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
