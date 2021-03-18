from pathfinder import PathFinder
from tMap import TMap
import sys
import time
#import resource

def main():
    tStart = time.time()
    # print(sys.getrecursionlimit())
    # resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
    sys.setrecursionlimit(0x100000)
    # print(sys.getrecursionlimit())
    # tMap = TMap("inputMaps/examples/Prob16.in.txt")
    tMap = TMap("inputMaps\\examples\\UltraHardTH.in.txt")
    pathfinder = PathFinder(tMap.startNode)
    print(f"\n\tsolution: {pathfinder.bestFound}\tInstances: {pathfinder.totalProcesses}")
    tFinish = time.time()
    tDif = (tFinish - tStart) * 1000 # execution time in ms
    print(f"\texecution time: {round(tDif, 3)} ms")

main()
