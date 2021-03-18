from numpy.lib.arraysetops import isin
import functions
from node import Node
from tMap import TMap

class PathFinder:
    
    def __init__(self, startNode, tMap):
        self.bestFound = None # lowest amount of steps found to reach goal
        self.totalProcesses = 0 # debugging

        self.torchValue = 15
        self.successfulPath = None

        self.tMap = TMap(tMap.inputFile) # debugging

        self.find(startNode, -1, self.torchValue + 1, [], [])
        
    # worse means step count is higher than node's count
    def stepCountWorse(self, stepCount, node):
        return (node.crMnStp != None and node.crMnStp <= stepCount) or (self.bestFound != None and self.bestFound <= stepCount)

    def torchLeftWorse(self, torchLeft, node):
        return (node.maxTorchLeft != None and node.maxTorchLeft >= torchLeft)

    def find(self, node, stepCount, torchLeft, torchList, path):
        
        #path = pathOld.copy()
        self.totalProcesses += 1 # debugging
        stepCount += 1
        torchLeft -= 1

        if torchLeft <= 0:
            return
        
        currentStepCountWorse = self.stepCountWorse(stepCount, node)
        currentTorchLeftWorse = self.torchLeftWorse(torchLeft, node)


        if currentStepCountWorse and currentTorchLeftWorse: # if pathfinder is in a worse (both step and torch) position, early return
            #print("torch or step failed")
            return
        
        node.crMnStp = functions.minWithNone(node.crMnStp, stepCount)
        node.setTorchLeft(torchLeft)

        if node.isTorch and not [node.i, node.j] in torchList:
            # print("Torch collected")
            torchList.append([node.i, node.j])
            torchLeft += self.torchValue

        
        if node.isGoal:
            #print(f"Goal found: {stepCount}\tPath length: {len(path)}")
            if functions.minWithNone(stepCount, self.bestFound) == stepCount:
                #print(f"Path set with length {stepCount}")
                self.successfulPath = path
            self.bestFound = functions.minWithNone(stepCount, self.bestFound)
            return

        # #if self.tMap.getNode(node.i, node.j).char == " " or self.tMap.getNode(node.i, node.j).char == "*":
        # self.tMap.getNode(node.i, node.j).char = "O" # debugging
        # input("") # debugging
        # print(self.tMap) # debugging
        # print(f"stepCount: {stepCount} (worse:{currentStepCountWorse})\ttorchLeft: {torchLeft} (worse:{currentTorchLeftWorse})\n")
        # if self.tMap.getNode(node.i, node.j).char == "O":
        #     self.tMap.getNode(node.i, node.j).char = " " # debugging

        for connectedNode in node.connections:
            path.append(connectedNode)
            pathNew = path.copy()
            path.pop(-1)
            newTorchList = torchList.copy()
            
            #print(f"stepCount: {stepCount}\tpos: {node.char}[{node.j}, {node.i}] -> {connectedNode.char}[{connectedNode.j}, {connectedNode.i}]") # debugging
            self.find(connectedNode, stepCount, torchLeft, newTorchList, pathNew)


def main():
    pass
