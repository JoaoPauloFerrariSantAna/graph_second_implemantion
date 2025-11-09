from typing import TypedDict
from node import Node  

Adjacencies = TypedDict("Adjacencies", { "vertices": list[str], "edges": list[Pairs] });
Degree = dict[str, dict[str, NodeTotal]]
NodeConnections = list[Node]
NodeInDegree = int
NodeList = dict[str, list[str]]
NodeNeighbors = list[str]
NodeOutDegree = int
NodeTotal = NodeOutDegree | NodeInDegree
Pairs = list[str]
Path = list[str]
