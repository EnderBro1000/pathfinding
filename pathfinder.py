from node import Node

class PathFinder:
    def __init__(self, startNode):
        self.bestFound = None # lowest amount of steps found to reach goal
        self.totalProcesses = 0


        self.find(startNode, -1)



    def find(self, node, stepCount):
        self.totalProcesses += 1
        stepCount += 1
        # print(f"proc: {self.totalProcesses}\tFound: {self.bestFound}\tstepCount: {stepCount}\tchar: '{node.char}'")
        #print(f"char: '{node.char}'\tstepCount: {stepCount}\tpos: [{node.x}, {node.y}]")
        # if pathfinder is worse than a found position or best position, early return
        if (node.crMnStp != None and node.crMnStp <= stepCount) or (self.bestFound != None and self.bestFound <= stepCount):
            #print("end instance")
            return

        node.crMnStp = stepCount

        # if stepCount != 0:
        #     if stepCount % 10 == 0:
        #         print("early end instance")
        #         return
        if node.isGoal:
            if (self.bestFound == None):
                self.bestFound = stepCount
            else:
                self.bestFound = min(stepCount, self.bestFound)
            #print(f"found: {self.bestFound} (end instance)")
            return
        
        for connectedNode in node.connections:
            #if stepCount > 100:
                #print(f"stepCount: {stepCount}\tpos: {node.char}[{node.x}, {node.y}] -> {connectedNode.char}[{connectedNode.x}, {connectedNode.y}]")
            self.find(connectedNode, stepCount)

def main():
    node = Node("H")
    node.crMnStp = -1
    
    test = PathFinder(node)
