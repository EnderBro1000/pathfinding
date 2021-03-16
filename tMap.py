import numpy as np
from mapParser import MapParser, stringToNodeMatrix
from node import Node

def matrixString(mat) -> str:
    out = ""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            out += f"{mat[i][j]} "
        out += "\n"
    return out

class TMap:
    def __init__(self, inputFile):

        startNode = None
        print("created map")
        self.nodeMatrix = MapParser.parse(inputFile)

        # self.nodeMatrix = np.flip(self.nodeMatrix)

        for i, rows in enumerate(self.nodeMatrix): ### # [1:-1]??????hlp????????????
            for j, node in enumerate(rows):
                if (node.isStart):
                    startNode = node
                if not node.isWall:
                    node.addOpenConnection(self.nodeMatrix[i][j-1]) # up
                    node.addOpenConnection(self.nodeMatrix[i][j+1]) # down
                    node.addOpenConnection(self.nodeMatrix[i-1][j]) # left
                    node.addOpenConnection(self.nodeMatrix[i+1][j]) # right


    def __repr__(self) -> str:
        return matrixString(self.nodeMatrix)
                

def main():
    # tMap = TMap("inputMaps/examples/Prob16.in.txt")
    tMap = TMap("inputMaps/mapTest.txt")
    
    print(tMap)
    print("Connections: ")
    print(Node.outAllConnections(tMap.nodeMatrix))
    
main()
