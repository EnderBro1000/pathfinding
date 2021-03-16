from node import Node


def minWithNone(a, b): # returns the min between a and b, or whichever is not None
    if a is None:
        return b
    elif b is None:
        return a
    return min(a,b)
    
def maxWithNone(a, b): # returns the max between a and b, or whichever is not None
    if a is None:
        return b
    elif b is None:
        return a
    return max(a,b)


class PathFinder:
    
    def __init__(self, startNode):
        self.bestFound = None # lowest amount of steps found to reach goal
        self.totalProcesses = 0 # debugging

        self.torchValue = 15

        self.find(startNode, -1, self.torchValue + 1)
        
    # worse means step count is higher than node's count
    def stepCountWorse(self, stepCount, node):
        return (node.crMnStp != None and node.crMnStp <= stepCount) or (self.bestFound != None and self.bestFound <= stepCount)

    def torchLeftWorse(self, torchLeft, node):
        return (node.maxTorchLeft != None and node.maxTorchLeft <= torchLeft)

    def find(self, node, stepCount, torchLeft):
        self.totalProcesses += 1 # debugging
        stepCount += 1
        torchLeft -= 1

        # if torchLeft <= 0:
        #     return
        
        currentStepCountWorse = self.stepCountWorse(stepCount, node)
        currentTorchLeftWorse = self.torchLeftWorse(torchLeft, node)

        if currentStepCountWorse: #and currentTorchLeftWorse: # if pathfinder is in a worse (both step and torch) position, early return
            return
        
        node.crMnStp = stepCount
        
        if node.isGoal:
            self.bestFound = minWithNone(stepCount, self.bestFound)
            return

        
        for connectedNode in node.connections:
            #print(f"stepCount: {stepCount}\tpos: {node.char}[{node.x}, {node.y}] -> {connectedNode.char}[{connectedNode.x}, {connectedNode.y}]") # debugging
            self.find(connectedNode, stepCount, torchLeft)


def main():
    pass
