from typing import Final
from node import Node
from important_types import(
	NodeNeighbors,
	NodeList,
	NodeConnections,
	NodeOutDegree,
	NodeInDegree,
	NodeTotal,
	Degree,
	Path
)

# TODO: maybe create a NodeException

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

	def __findOutDegrees(self, verticeName: str) -> NodeOutDegree:
		# here we need the length 'cause we are intrepreting the length
		# as the out degree, because if node A is connecting to other three
		# nodes, then we will have three connections coming OUT from A
		return len(self.__edges[verticeName])

	def __findInDegrees(self, verticeName: str, vertices: NodeNeighbors) -> NodeInDegree:
		# now to get the IN degree, we will need to go back to the start of the graph
		# and search for which node is coming in to vertice
		# we need to get the items 'cause then if we get to the key that is verticeName
		# we will be making things wrong
		din = 0

		if(verticeName in vertices):
			din += 1

		return din

	def getNeighbors(self, verticeName: str) -> NodeNeighbors:
		if(verticeName not in self.__edges):
			raise Exception(f"Node '{verticeName}' unknown!")

		return self.__edges[verticeName]

	def getDegreesFrom(self, vertice: Node) -> Degree:
		totalDegrees = {}

		for k,v in self.__edges.items():
			totalDegrees[k] = {
				"din": 0,
				"dout": 0,
				"total": 0
			}

			din = 0
			dout = 0
			total = 0

			dout = self.__findOutDegrees(k)

			# this is looping through self.__edges[verticeName] by the way
			# but it'll find nothing
			din = self.__findInDegrees(vertice.getNodeName(), v)
			total = dout + din

			totalDegrees[k]["dout"] = dout
			totalDegrees[k]["din"] = din
			totalDegrees[k]["total"] = total

		return totalDegrees

	def isPathValid(self, path: Path) -> bool:
		if(self.__isTrivial(len(path))): return True

		edges = self.__edges

		for i in range(len(path) - 1):
			testVertice = (path[i], path[i+1])

			if(not self.__inEdge(testVertice[0], testVertice[1])):
				return False

		return True

	def appendEdge(self, edgeToAppend: Node) -> None:
		self.__edges[edgeToAppend.getNodeName()] = edgeToAppend.getConnections()

	def removeVertice(self, edgeToRemove: Node) -> None:
		edges = self.__edges
		nameOfEdge = edgeToRemove.getNodeName()

		if(nameOfEdge not in edges):
			raise Exception(f"Edge {edgeToRemove.getNodeName()} does not exists")

		for vertices in edges.values():
			for i in range(len(vertices)):
				if(vertices[i] == nameOfEdge): vertices[i] = None

		# TODO: remove this del
		del edges[nameOfEdge]

	def getEdges(self) -> NodeList:
		return self.__edges
