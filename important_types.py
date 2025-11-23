from typing import TypedDict
from node import Node  

Pairs = list[str]
Adjacencies = TypedDict("Adjacencies", { "vertices": list[str], "edges": list[Pairs] });
Degree = dict
NodeInDegree = int
NodeOutDegree = int
NodeTotal = NodeOutDegree | NodeInDegree
NodeConnections = list[Node]
NodeList = dict[str, list[str]]
NodeNeighbors = list[str]
Path = list[str]
