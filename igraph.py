from abc import ABC, abstractmethod
from node import Node
from important_types import(
    NodeNeighbors,
    NodeOutDegree,
    NodeInDegree,
    Degree,
    Path
)

class IGraph(ABC):
    @abstractmethod
    def __init__() -> None:
        pass

    @abstractmethod
    def __findOutDegrees(self, verticeName: str) -> NodeOutDegree:
        pass

    @abstractmethod
    def __findInDegrees(self, verticeName: str, vertices: NodeNeighbors) -> NodeInDegree:
        pass

    @abstractmethod
    def getNeighbors(self, verticeName: str) -> NodeNeighbors:
        pass

    @abstractmethod
    def getDegreesFrom(self, vertice: Node) -> Degree:
        pass

    @abstractmethod
    def isPathValid(self, path: Path) -> bool:
        pass