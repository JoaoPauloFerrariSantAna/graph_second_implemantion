from typing import Final
from node import Node
from main_types import NodeList, Path

MINIMAL_TRIVIAL_LENGTH: Final = 2

class Graph():
    """Represents a undirected graph with Nodes.
    
    Keyword arguments:

    :param edges: the dictionary to represent the graph as a whole.
    """
    def __init__(self, edges: NodeList) -> None:
        self.__edges = edges

    # TODO: create a setEdges
    
    def __isTrivial(self, pathLength: int) -> bool:
        return (pathLength < MINIMAL_TRIVIAL_LENGTH)
    
    def __inEdge(self, origin, dest) -> bool:
        if(origin in self.__edges and dest in self.__edges[origin]):
            return True
        
        return False

    def isPathValid(self, path: Path) -> bool:
        if(self.__isTrivial(len(path))): return True

        edges = self.__edges

        for i in range(len(path) - 1):
            testVertice = (path[i], path[i+1])

            if(not self.__inEdge(testVertice[0], testVertice[1])):
                return False

        return True

    def appendEgde(self, edgeToAppend: Node) -> None:
        self.__edges[edgeToAppend.getNodeName()] = edgeToAppend.getConnections()

    def removeVertice(self, edgeToRemove: Node) -> None:
        edges = self.__edges
        nameOfEdge = edgeToRemove.getNodeName()

        if(nameOfEdge not in edges): raise NotImplementedError

        for vertices in edges.values():
            for i in range(len(vertices)):
                if(vertices[i] == nameOfEdge): vertices[i] = None

        # TODO: remove this del
        del edges[nameOfEdge]

    def getEdges(self) -> NodeList:
        return self.__edges