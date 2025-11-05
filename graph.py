from node import Node
from main_types import NodeList

class Graph():
    """Represents a undirected graph with Nodes.
    
    Keyword arguments:

    :param edges: the dictionary to represent the graph as a whole.
    """
    def __init__(self, edges: NodeList) -> None:
        self.__edges = edges

    def appendEgde(self, edgeToAppend: Node) -> None:
        self.__edges[edgeToAppend.getNodeName()] = edgeToAppend.getConnections()

    def removeVertice(self, edgeToRemove: Node) -> None:
        edges = self.__edges
        nameOfEdge = edgeToRemove.getNodeName()

        if(nameOfEdge not in edges): raise NotImplementedError

        for vertices in edges.values():
            for i in range(len(vertices)):
                if(vertices[i] == nameOfEdge): vertices[i] = None

        del edges[nameOfEdge]

    def getEdges(self) -> NodeList:
        return self.__edges