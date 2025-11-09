from node import Node
from important_types import Adjacencies, Degree, NodeNeighbors

# TODO: work on something if we only have one Node in edgesList

class AdjacencyList():
	"""Represents a adjancency list of an undirected graph with Nodes."""
	# for now the idea is to just add the graph as dependency
	def __init__(self) -> None:
		self.__adjacencylist: Adjacencies = { "vertices": [], "edges": [] }

	def __removeInVertices(self, verticeName) -> None:
		verticesList = self.__adjacencylist["vertices"]

		for verticeInList in verticesList:
			if(verticeName == verticeInList):
				verticesList.remove(verticeInList)
	
	def __removeInEdges(self, verticeName: list) -> None:
		edgesList = self.__adjacencylist["edges"]

		for pair in range(len(edgesList)):
			for nodeName in edgesList[pair]:
				if(verticeName == nodeName):
					edgesList[pair].remove(nodeName)
	
	def __isThereNeighbors(self, pairToCheck, existingPair) -> bool:
		origin = pairToCheck[0]
		dest = pairToCheck[1]

		# since it is not directed, we may have BA or AB
		return ((origin == existingPair[0] and dest == existingPair[1]) or (dest == existingPair[0] and origin == existingPair[1]))

	def appendVertice(self, vertice: str) -> None:
		if(vertice in self.__adjacencylist["vertices"]):
			raise Exception(f"Vertice {vertice} already exists in list")

		self.__adjacencylist["vertices"].append(vertice)
	
	def appendEdge(self, edge: str, origin: str, dest: str) -> None:
		if(origin not in self.__adjacencylist["vertices"] or dest not in self.__adjacencylist["vertices"]):
			raise Exception("Edge does not exists in list")

		self.__adjacencylist["edges"].append([origin, dest])
		self.__adjacencylist["edges"].append([dest, origin])
	
	def removeVertice(self, verticeName: str) -> None:
		self.__removeInVertices(verticeName)
		self.__removeInEdges(verticeName)
	
	def doesEdgeExists(self, pairToSearch: Pairs) -> bool:
		edgesList = self.__adjacencylist["edges"]

		for pair in range(len(edgesList)):
			if(self.__isThereNeighbors(pairToSearch, edgesList[pair])):
				return True

		return False
	
	def getNeighboorsFrom(self, verticeName: str, pair: Pairs) -> NodeNeighbors:
		neighboors = []

		for origin in range(len(pair)-1):
			if(verticeName == pair[origin]):
				neighboors.append(pair[origin+1])

		return neighboors

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

			raise NotImplementedError

	def getAdjacenyList(self) -> Adjacencies:
		return self.__adjacencylist
