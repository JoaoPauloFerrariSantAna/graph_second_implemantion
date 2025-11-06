from node import Node  

# like a matrix
NodeNeighbors = list[str]
NodeList = dict[str, list[str]]
NodeOutDegree = int
NodeInDegree = int
NodeTotal = NodeOutDegree | NodeInDegree
NodeConnections = list[Node]
Path = list[str]
Degree = dict[str, dict[str, NodeTotal]]
